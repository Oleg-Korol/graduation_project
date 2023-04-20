
from uuid import uuid4
from datetime import datetime
from .models import Car
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender=Car,dispatch_uid = uuid4())
def create_custom(sender,**kwargs):
    new = Car.objects.last()

    time=datetime.now()

    with open("static/txt/Postavki.txt",  'a',encoding='utf-8') as file:
        file.write(f" {time} Добавился новый {new.last_name} на склад!"
                   f"Cтоимость {new.price}."
                   f" Подробная информация у менеджера по продажам"+ '\n')
        file.write('-' * 110 + "\n")
