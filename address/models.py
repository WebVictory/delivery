from django.db import models

class Delivery(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=200)
    type = models.CharField(verbose_name='Тип товара',max_length=200)
    date_delivery = models.DateTimeField('Дата доставки')
    file = models.FileField(verbose_name='Файл', upload_to='files/')

    def get_absolute_url(self):
        return '/success/'

    def __str__(self):
        return self.name

class Address(models.Model):
    address = models.CharField(max_length=200, verbose_name='Адрес доставки')
    delivery = models.ForeignKey(Delivery, models.CASCADE, verbose_name='Заказ')