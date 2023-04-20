from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .forms import ManagerFormAdmin
from .models import *

class CarAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'year_of_release','type_body',
                    'volume_engine','fuel','avtosalon_group']
    list_display_links = ['last_name']
    ordering = ['last_name','fuel','type_body','year_of_release']
    list_filter = ['last_name','fuel','type_body']
    list_per_page = 5
    search_fields = ['last_name','fuel','type_body']

class ManufactureAdmin(admin.ModelAdmin):
    list_display = ['manufacture_name', 'country_of_manufacture','logo_manuf']
    list_display_links = ['manufacture_name']
    ordering = ['country_of_manufacture']
    list_filter = ['country_of_manufacture']
    list_per_page = 5
    search_fields = ['manufacture_name', 'country_of_manufacture']


class StockAdmin(admin.ModelAdmin):
    list_display = ['name', 'sity','location','top_manager']
    list_display_links = ['name']
    ordering = ['name']
    list_filter = ['sity']
    list_per_page = 5
    search_fields = ['sity', 'name']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name_team', 'top_employee']
    list_display_links = ['name_team', 'top_employee']
    ordering = ['name_team']
    list_filter = ['name_team']
    list_per_page = 5
    search_fields = ['name_team', 'top_employee']



class Shop_manager_Admin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'patronymic', 'manager_team',
                    'custom_field', 'ava']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['manager_team']
    list_filter = ['last_name',
                   'first_name',
                   'patronymic',
                   'manager_team',
                   'phone_number',
                   ]
    search_fields = ['last_name']
    list_per_page = 5
    ordering = ['last_name']
    form = ManagerFormAdmin

    @staticmethod
    def ava(obj):
        return mark_safe(f'<img src="{obj.avatar.url}"width="100">')

    @staticmethod
    def custom_field(obj):
        return mark_safe('<a href ="https://www.google.ru">Google</a>')

    # @staticmethod
    # def view_on_site(obj):
    #      return reverse('shop_manager-edit',kwargs = {'pk':obj.id})

class SaleAdmin(admin.ModelAdmin):
    list_display = ['sale_name', 'discount_amount']
    list_display_links = ['sale_name']
    ordering = ['sale_name']
    list_filter = ['discount_amount']
    list_per_page = 5
    search_fields = ['sale_name', 'discount_amount']

class ServiseAdmin(admin.ModelAdmin):
    list_display = ['car_brand', 'to_0_price',
                    'to_1_price','to_2_price',
                    'to_3_price','to_4_price',
                    'to_5_price','to_6_price']
    list_display_links = ['car_brand']
    ordering = ['car_brand']
    list_filter = ['car_brand']
    list_per_page = 5
    search_fields = ['car_brand']

class RecordServiseAdmin(admin.ModelAdmin):
    list_display = ['time_servise','first_name', 'car_model',
                    'type_of_repair','service',
                    'client_email','phone_number']
    list_display_links = ['first_name']
    ordering = ['time_servise']
    list_filter = ['time_servise']
    list_per_page = 5
    search_fields = ['first_name']


# Register your models here.
admin.site.register(Car,CarAdmin)
admin.site.register(Stock,StockAdmin)
admin.site.register(Manufacture,ManufactureAdmin)
# admin.site.register(Manager)
admin.site.register(Shop_manager, Shop_manager_Admin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Auto_service,ServiseAdmin)
admin.site.register(Sale,SaleAdmin)
# admin.site.register(MothJournal)
admin.site.register(Topic)
admin.site.register(Record,RecordServiseAdmin)
