from mainapp.models import Record

from django.conf import settings
from config.celery import app

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from email.mime.application import MIMEApplication

import datetime
import pandas as pd
import os





@app.task
def message_user(user_mail,name):

    """отправляет письмо на почту записавшемуся клиенту"""

    subject = 'Джанго приложение'
    message = f'Привет {name}. Ваша заявка принята'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_mail, ]
    send_mail(subject, message, email_from, recipient_list)





@app.task
def message_me():

    """собирает и отправляет отчет об актуальных заявках на
                    данный момент времени"""

    rec = Record.objects.all()
    slv = {}
    for i in rec:
        if i.time_servise > datetime.date.today():
            slv.setdefault('Имя клиента', []).append(i.first_name)
            slv.setdefault('Марка авто', []).append(i.car_model)
            slv.setdefault('Вид технического обслуживания', []).append(
                i.type_of_repair)
            slv.setdefault('Номер телефона', []).append(i.phone_number)
            slv.setdefault('Салон', []).append(i.service)
            slv.setdefault('Email', []).append(i.client_email)
            slv.setdefault('Дата',[]).append(i.time_servise)

    new = pd.DataFrame(slv)

    new.to_excel("D:/new_otchet.xlsx")
    my_email = os.getenv('my_email')
    my_email2 = os.getenv('my_email2')


    email = EmailMessage(
        'Актуальные заявки',
        'Отчет.Приложение',
        my_email2,
        [my_email],
    )

    attachmentPath = "D:\\new_otchet.xlsx"
    with open(attachmentPath, "rb") as attachment:
        p = MIMEApplication(attachment.read(), _subtype="xlsx")
        p.add_header('Content-Disposition',
                     "attachment; filename= %s" %
                     attachmentPath.split("\\")[-1])
    email.attach(p)
    email.send()

    if os.path.isfile('D:\\new_otchet.xlsx'):
        os.remove('D:\\new_otchet.xlsx')
        print("Фаил очищен")
    else:
        print("Фаил не был записан!")


