
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


#  модель автомобиля
class Car(models.Model):
    """"Car models"""

    class Meta:
        verbose_name = u'Автомобиль'
        verbose_name_plural = u'Автомобили'

    car_name = models.ForeignKey('Manufacture',
                                 verbose_name=u'Марка автомобиля',
                                 blank=False,
                                 null=True,
                                 on_delete=models.PROTECT)
    last_name = models.CharField(max_length=100,
                                 blank=False,
                                 verbose_name=u"Модель автомобиля")
    vin = models.CharField(max_length=17,
                           blank=True,
                           null=False,
                           verbose_name=u"Вин номер")
    car_class = models.CharField(max_length=2,
                                 blank=True,
                                 null=False,
                                 verbose_name=u"Класс автомобиля")
    year_of_release = models.IntegerField(blank=False,
                                          verbose_name=u"Год выпуска")
    type_body = models.CharField(max_length=50,
                                 blank=False,
                                 verbose_name=u"Тип кузова")
    drive = models.CharField(max_length=50,
                             blank=False,
                             verbose_name=u"Тип привода")
    fuel = models.CharField(max_length=50,
                            blank=False,
                            verbose_name=u"Вид топлива")
    volume_engine = models.FloatField(blank=False,
                                      verbose_name=u"Рабочий обьем,куб.см")
    color = models.CharField(max_length=50, blank=False, verbose_name=u"Цвет")
    number_of_seats = models.IntegerField(blank=False,
                                          verbose_name=u"Колличество мест")
    maximum_speed = models.IntegerField(blank=False,
                                        verbose_name=u"Максю скорость,км/ч")
    curb_weight = models.IntegerField(blank=False,
                                      verbose_name=u"Снаряженная масса,кг")
    euroncap = models.IntegerField(blank=False,
                                   verbose_name=u"Рейтинг безопасности ")
    price = models.IntegerField(blank=False, verbose_name=u"Цена(y.e.)")
    sale_price = models.IntegerField(blank=True, null=True,
                                     verbose_name=u"Цена c учетом скидки(y.e.)")
    photo = models.ImageField(blank=True, null=True, verbose_name=u"Фото",
                              upload_to='image_car')
    notes = models.TextField(blank=True, verbose_name=u"Доп. информация")
    create_at = models.DateTimeField(auto_created=True)
    avtosalon_group = models.ForeignKey('Stock', verbose_name=u'Автосалон',
                                        blank=False, null=True,
                                        on_delete=models.PROTECT)

    def __str__(self):
        return f'Автомобиль {self.car_name} {self.last_name}'


class Manufacture(models.Model):
    """"Manufacture model"""

    class Meta:
        verbose_name = u"Производитель"
        verbose_name_plural = u'Производители'

    manufacture_name = models.CharField(max_length=50, blank=False,
                                        verbose_name=u"Названия компании")
    country_of_manufacture = models.CharField(max_length=50, blank=False,
                                              verbose_name=u"Страна производства")
    date_of_foundation = models.CharField(max_length=50, blank=False,
                                          verbose_name=u"Дата основания компании")
    history = models.TextField(blank=True, null=True,
                               verbose_name=u"История компании")
    logo_manuf = models.ImageField(blank=True, null=True,
                                   verbose_name=u"Логотип", upload_to='logo')

    def __str__(self):
        return f'Производитель - {self.manufacture_name} - ' \
               f'страна {self.country_of_manufacture}'


# Салоны
class Stock(models.Model):
    """"Stock model"""

    class Meta:
        verbose_name = u"Салон"
        verbose_name_plural = u'Салоны'

    name = models.CharField(max_length=50, blank=False,
                            verbose_name=u"Название салона")
    sity = models.CharField(max_length=50, blank=False, verbose_name=u"Город")
    location = models.CharField(max_length=50, blank=False,
                                verbose_name=u"Адрес")
    square = models.IntegerField(blank=True, null=True,
                                 verbose_name=u"Площадь склада,м.кв")
    number_of_seats = models.IntegerField(blank=True, null=True,
                                          verbose_name=u"Количество мест на складе")
    manager_shop = models.ForeignKey('Shop_manager',
                                     verbose_name=u'Менедер по продажам',
                                     blank=False, null=True,
                                     on_delete=models.PROTECT)
    top_manager = models.ForeignKey('Manager', verbose_name=u'Управляющий',
                                    blank=False, null=True,
                                    on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=50, blank=False,
                                    verbose_name=u"Номер телефона")
    foto = models.ImageField(blank=True, null=True,
                             verbose_name=u"Фото шоурума",
                             upload_to='foto_salon')

    def __str__(self):
        return f'Cалон по продаже автомобилей {self.name} ' \
               f'расположенный в городе {self.sity} по адресу {self.location}'


class Manager(models.Model):
    """"Manager model"""

    class Meta:
        verbose_name = u"Управляющий"
        verbose_name_plural = u'Управляющие'

    first_name = models.CharField(max_length=50, blank=False,
                                  verbose_name=u"Имя")
    last_name = models.CharField(max_length=50, blank=False,
                                 verbose_name=u"Фамилия")
    patronymic = models.CharField(max_length=50, blank=False,
                                  verbose_name=u"Отчество")
    phone_number = models.CharField(max_length=50, blank=False,
                                    verbose_name=u"Номер телефона")
    number_tm = models.IntegerField(blank=False, null=False,
                                    verbose_name=u"Табельный номер")
    create_at = models.DateTimeField(auto_created=True)
    avatar = models.ImageField(blank=True, null=True, verbose_name=u"Аватар",
                               upload_to='ava')

    def __str__(self):
        return f'Управляющий  {self.first_name} {self.last_name}' \
               f' {self.patronymic} '


class Shop_manager(models.Model):
    """"Manager shop"""

    class Meta:
        verbose_name = u"Менеджер по продажам"
        verbose_name_plural = u'Менеджеры по продажам'

    first_name = models.CharField(max_length=50, blank=False,
                                  verbose_name=u"Имя")
    last_name = models.CharField(max_length=50, blank=False,
                                 verbose_name=u"Фамилия")
    patronymic = models.CharField(max_length=50, blank=False,
                                  verbose_name=u"Отчество")
    phone_number = models.CharField(max_length=50, blank=False,
                                    verbose_name=u"Номер телефона")
    number_tm = models.IntegerField(blank=False, null=False,
                                    verbose_name=u"Табельный номер")
    manager_team = models.ForeignKey('Team', verbose_name=u'Подразделение',
                                     blank=False, null=True, default='',
                                     on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_created=True)
    avatar = models.ImageField(blank=True, null=True, verbose_name=u"Аватар",
                               upload_to='ava')

    def __str__(self):
        return f'Менеджер  {self.first_name} {self.last_name} {self.patronymic} '


class Team(models.Model):
    """"Stock model"""

    class Meta:
        verbose_name = u"Отдел"
        verbose_name_plural = u'Отделы'

    name_team = models.CharField(max_length=50, blank=False,
                                 verbose_name=u"Название отдела")
    create_at = models.DateTimeField(auto_created=True,
                                     verbose_name=u"Дата основания отдела")
    top_employee = models.OneToOneField('Shop_manager',
                                        verbose_name=u"Сотрудник месяца",
                                        blank=True, null=True,
                                        on_delete=models.SET_NULL)

    def __str__(self):
        return f"<{self.name_team}>"


class Sale(models.Model):
    """Sales model"""

    class Meta:
        verbose_name = u"Скидка"
        verbose_name_plural = u'Скидки'

    sale_name = models.CharField(max_length=50, blank=True, null=False,
                                 verbose_name=u"Название акции")
    discount_amount = models.IntegerField(blank=False, null=False,
                                          verbose_name=u"Размер скидки")

    def __str__(self):
        return f'Скидки  {self.discount_amount} % '


class BaseContenerAuto(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100)

    create_ad = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False, null=True,
    )

    update_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False, null=True,
    )

    delete_at = models.CharField(default=False, max_length=10)

    def delete(self):
        self.delete_at = True
        self.save()


class MothJournal(models.Model):
    class Meta:
        verbose_name = u"Журнал учета рабочего времени"
        verbose_name_plural = u'Журналы учета рабочего времени'

    employee = models.ForeignKey('Shop_manager',
                                 verbose_name="Сотрудник",
                                 blank=False,
                                 unique_for_month='date',
                                 on_delete=models.PROTECT,
                                 )

    date_journal = models.DateTimeField(blank=False)

    present_day_1 = models.BooleanField(default=False)
    present_day_2 = models.BooleanField(default=False)
    present_day_3 = models.BooleanField(default=False)
    present_day_4 = models.BooleanField(default=False)
    present_day_5 = models.BooleanField(default=False)
    present_day_6 = models.BooleanField(default=False)
    present_day_7 = models.BooleanField(default=False)
    present_day_8 = models.BooleanField(default=False)
    present_day_9 = models.BooleanField(default=False)
    present_day_10 = models.BooleanField(default=False)
    present_day_11 = models.BooleanField(default=False)
    present_day_12 = models.BooleanField(default=False)
    present_day_13 = models.BooleanField(default=False)
    present_day_14 = models.BooleanField(default=False)
    present_day_15 = models.BooleanField(default=False)
    present_day_16 = models.BooleanField(default=False)
    present_day_17 = models.BooleanField(default=False)
    present_day_18 = models.BooleanField(default=False)
    present_day_19 = models.BooleanField(default=False)
    present_day_20 = models.BooleanField(default=False)
    present_day_21 = models.BooleanField(default=False)
    present_day_22 = models.BooleanField(default=False)
    present_day_23 = models.BooleanField(default=False)
    present_day_24 = models.BooleanField(default=False)
    present_day_25 = models.BooleanField(default=False)
    present_day_26 = models.BooleanField(default=False)
    present_day_27 = models.BooleanField(default=False)
    present_day_28 = models.BooleanField(default=False)
    present_day_29 = models.BooleanField(default=False)
    present_day_30 = models.BooleanField(default=False)


class Auto_service(BaseContenerAuto):
    car_brand = models.CharField(max_length=100)
    to_0 = models.CharField(max_length=100)
    to_0_price = models.IntegerField(blank=False, null=True)
    to_1 = models.CharField(max_length=100)
    to_1_price = models.IntegerField(blank=False, null=True)
    to_2 = models.CharField(max_length=100)
    to_2_price = models.IntegerField(blank=False, null=True)
    to_3 = models.CharField(max_length=100)
    to_3_price = models.IntegerField(blank=False, null=True)
    to_4 = models.CharField(max_length=100)
    to_4_price = models.IntegerField(blank=False, null=True)
    to_5 = models.CharField(max_length=100)
    to_5_price = models.IntegerField(blank=False, null=True)
    to_6 = models.CharField(max_length=100)
    to_6_price = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'Регламент ТО  на автомобиле {self.car_brand} '


class Topic(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title


class Record(models.Model):
    """"Record model"""

    class Meta:
        verbose_name = u"Запись на сервис"
        verbose_name_plural = u'Записи на сервисное обслуживание'

    first_name = models.CharField(max_length=50, blank=False,
                                  verbose_name=u"Имя")
    car_model = models.CharField(max_length=50, blank=False,
                                 verbose_name=u"Модель автомобиля")
    type_of_repair = models.CharField(max_length=50, blank=False,
                                      verbose_name=u"Вид технического обслуживания")
    phone_number = models.CharField(max_length=50, blank=False,
                                    verbose_name=u"Номер телефона")
    create_at = models.DateTimeField(auto_created=True,
                                     verbose_name=u"Дата записи  на ТО")
    service = models.ForeignKey('Stock',
                                verbose_name=u"Выберите салон",
                                blank=True, null=True,
                                on_delete=models.SET_NULL)
    client_email = models.EmailField(verbose_name=u'Email',
                                     blank=False,
                                     null=True)

    time_servise = models.DateField(verbose_name=u"День  ТО")

    def __str__(self):
        return f'Автомобиль {self.car_model}.,' \
               f'Необходимо выполнить  {self.type_of_repair}.,' \
               f'Номер телефона {self.phone_number}.' \
               f'Имя клиента {self.first_name}.,' \
               f'Выбор сервиса:  {self.service}'

















