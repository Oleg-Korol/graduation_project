from django.conf.urls import url

from . import views
from django.urls import path

# from .views import JournalView

urlpatterns = [
    path('',views.index,name = "home"),
    path('cars',views.cars,name =  'avto'),
    path('manufacture',views.manufacture,name =  'manufacture'),
    path('salon',views.salon,name =  'salon'),
    path('manager',views.manager,name =  'manager'),
    path('manshop',views.manager_shop,name =  'manager_shop'),
    path('service',views.auto_service,name = 'service'),
    path('personal',views.personal,name =  'personal'),
    path('about',views.about,name =  'about'),
    path('contact',views.topic,name =  'contact'),
    path('bmw',views.bmw,name =  'bmw'),
    path('opel',views.opel,name =  'opel'),
    path('lada',views.lada,name =  'lada'),
    path('peugeot',views.peugeot,name =  'peugeot '),
    path('ford',views.ford,name =  'ford '),
    path('renault',views.renault,name =  'renault '),
    path('honda',views.honda,name =  'honda '),
    path('mazda',views.mazda,name =  'mazda '),
    path('avtomoll',views.avtomoll,name =  'avtomoll'),
    path('shourum',views.shourum,name =  'shourum'),
    path('serv',views.auto_service,name =  'serv'),
    # url(r'^journal/(?P<pk>\d +)?/?$',JournalView.as_view(),name =  'journal'),
    # url(r'^team/add/$',views.TeamAddView.as_view(),name='team_add'),
    # url(r'^service/add/$',views.RecordAddView,name='record_add')
    url(r'^service/add/$',views.RecordAddView.as_view(),name='record_add')
    ]

