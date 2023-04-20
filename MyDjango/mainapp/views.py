# from calendar import monthrange, day_abbr, weekday
# from datetime import datetime
# from datetime import date
#
# from dateutil.relativedelta import relativedelta
# from django.db.models import QuerySet
from django.http import JsonResponse, HttpResponseRedirect
# from django.template import RequestContext
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from .forms import RecordForm

from .models import *
from django.shortcuts import render

from django.views.decorators.cache import cache_page

from .models import Manufacture
from .tasks import message_user
from .utils import sales



@cache_page(60 * 15)
def index(request):
    return render(request, 'mainapp/index.html', {'title': 'Главная страница'})

@cache_page(60 * 15)
def manufacture(request):
     man = Manufacture.objects.all()
     return render(request, 'mainapp/man_list.html',
                 {'title': 'Автомобили', 'man': man})


@cache_page(60 * 15)
def cars(request):
    sale_car = sales(request)
    sale = Sale.objects.all()
    return render(request, 'mainapp/sale_car_list.html',
                  {'title': 'Акции', 'auto': sale_car, 'sales': sale})


def salon(request):
    salon = Stock.objects.all()
    return render(request, 'mainapp/salon.html',
                  {'title': 'Наши салоны', 'salon': salon})


def personal(request):
    return render(request, 'mainapp/personal.html')


def manager(request):
    manager = Manager.objects.all()
    return render(request, 'mainapp/manager.html',
                  {'title': 'Руководство компании', 'manager': manager})


def manager_shop(request):
    manshop = Shop_manager.objects.all()
    return render(request, 'mainapp/manager_shop.html',
                  {'title': 'Менеджеры продаж', 'manshop': manshop})


def auto_service(request):
    serv = Auto_service.objects.filter(delete_at=False)
    return render(request,'mainapp/service.html',
                  {'title': 'Отдел сервисного обслуживаания',
                   'serv': serv})

def about(request):
    return render(request, 'mainapp/about.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def bmw(request):
    bmw = Car.objects.all().filter(car_name__manufacture_name='Bmw')
    return render(request, 'mainapp/bmw.html',
                  {'title': 'Автомобили  Bmw в наличии', 'bmw': bmw})


def opel(request):
    opel = Car.objects.all().filter(car_name__manufacture_name='Opel')
    return render(request, 'mainapp/opel.html',
                  {'title': 'Автомобили  Opel в наличии', 'opel': opel})


def lada(request):
    lada = Car.objects.all().filter(car_name__manufacture_name='Lada')
    return render(request, 'mainapp/lada.html',
                  {'title': 'Автомобили  Lada в наличии', 'lada': lada})


def peugeot(request):
    peugeot = Car.objects.all().filter(car_name__manufacture_name='Peugeot')
    return render(request, 'mainapp/peugeot.html',
                  {'title': 'Автомобили  Peugeot в наличии',
                   'peugeot': peugeot})


def ford(request):
    ford = Car.objects.all().filter(car_name__manufacture_name='Ford')
    return render(request, 'mainapp/ford.html',
                  {'title': 'Автомобили  Ford в наличии', 'ford': ford})


def renault(request):
    renault = Car.objects.all().filter(car_name__manufacture_name='Renault')
    return render(request, 'mainapp/renault.html',
                  {'title': 'Автомобили  Renault в наличии',
                   'renault': renault})


def honda(request):
    honda = Car.objects.all().filter(car_name__manufacture_name='Honda')
    return render(request, 'mainapp/honda.html',
                  {'title': 'Автомобили  Honda в наличии', 'honda': honda})


def mazda(request):
    mazda = Car.objects.all().filter(car_name__manufacture_name='Mazda')
    return render(request, 'mainapp/mazda.html',
                  {'title': 'Автомобили  Mazda в наличии', 'mazda': mazda})


def avtomoll(request):
    avtomoll = Car.objects.all().filter(avtosalon_group__name="АвтоМолл")
    return render(request, 'mainapp/avtomoll.html',
                  {'title': 'Автомобили  в  салоне Автомолл',
                   'avtomoll': avtomoll})


def shourum(request):
    shourum = Car.objects.all().filter(avtosalon_group__name="Шоурум")
    return render(request, 'mainapp/shourum.html',
                  {'title': 'Автомобили  в  салоне Шоурум',
                   'shourum': shourum})

def topic(request):
    topic = Topic.objects.all()
    return render(request, 'mainapp/contact.html',
                  {'title': 'Новостной блог',
                   'topic': topic})




# class JournalView(TemplateView):
#     template_name = 'mainapp/journal.html'
#
#     # get context from TemplateView class
#     def get_context_data(self, **kwargs):
#         context = super(JournalView,self).get_context_data(**kwargs)
#
#          #check if we need to display some specific month
#         if self.request.GET.get('month'):
#             month = datetime.strptime(
#                 self.request.GET['month'],
#                 '%Y-%m-%d',
#             ).date()
#         else:
#             today = datetime.today()
#             month = date(today.year,today.month,1)
#
#         # calculate current, previous and next month detail
#
#         next_month = month + relativedelta(month= 1 )
#         prev_month = month - relativedelta(month= 1 )
#
#         context['next.month'] = next_month.strftime('%Y-%m-%d')
#         context['prev.month'] = prev_month.strftime('%Y-%m-%d')
#         context['year'] = month.year
#         context['moth_verbose'] = month.strftime('%B')
#
#         context['cur_month'] = month.strftime('%Y-%m-%d')
#
#         m_year,m_month = month.year,month.month
#
#         number_of_days = monthrange(m_year,m_month)[1]
#         context['month_header'] = [{
#             'day': d,
#             'verbose':day_abbr[weekday(m_year,m_month,d)][:2]
#             } for d in range(1,number_of_days + 1)
#         ]
#
#         if kwargs.get('pk'):
#             queryset =[Shop_manager.objects.get(pk = kwargs.get['pk'])]
#
#         else:
#             queryset = Shop_manager.objects.all().order_by('last_name')
#
#         update_url = reverse('journal')
#
#         managers =[]
#
#
#         for manager in queryset:
#             try:
#                journal = MothJournal.objects.get(employee=manager,
#                                                  date_journal=month)
#             except MothJournal.DoesNotExist:
#                journal = None
#
#             days = []
#             for day in range (1,number_of_days +1):
#                 days.append({
#                     'day':day,
#                     'present':journal and getattr(
#                         journal,f'present_day_{day}',False,
#                     ) or False,
#                     'date':date(m_year,m_month,day).strftime('%Y-%m-%d')
#                 })
#
#             managers.append({
#                 'fullname':f'{manager.last_name}{manager.first_name}',
#                 'days':days,
#                 'id':manager.id,
#                 'update_url': update_url,
#
#             })
#             context['managers'] = managers
#
#             return context
#
#
#     def post(self,request,*args,**kwargs):
#         data = request.POST
#
#         current_date = datetime.strptime(data['date'],'%Y-%m-%d').date()
#         month = date(current_date.year,current_date.month,1)
#         present= date['present'] and True or False
#         manager = Shop_manager.objects.get(pk = date['pk'])
#
#         journal = MothJournal.objects.get_or_create(manager = manager,
#                                                     date_journal=month)[0]
#
#         setattr(journal,f'present_day {current_date.day}',present)
#         journal.save()
#
#         return JsonResponse({'status':'success'})
#




class RecordAddView(CreateView):
    model =Record
    template_name = 'mainapp/record_add.html'
    form_class = RecordForm

    def get_success_url(self):
        record = Record.objects.last()
        user_mail = record.client_email
        name = record.first_name
        message_user.delay(user_mail,name)
        return (f'{reverse("serv")}?status_massage=Изменения успешно сохранены!'
        )

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                f'{reverse("serv")} ?status_massage = Изменения отменены!'
            )
        return super(RecordAddView,self).post(
            request,*args,**kwargs,
        )







