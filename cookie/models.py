from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    photo = models.ImageField(upload_to='cookie/media', verbose_name='Фото', null=True)
    description = models.TextField(max_length=76, null=True, verbose_name='Описание')
    display = models.BooleanField(default=False, verbose_name='Показывать')
    priority = models.IntegerField(default=0, verbose_name='Приоритет')
    for_main = models.BooleanField(default=False, verbose_name='Показывать на главной')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    photo_for_slider = models.ImageField(upload_to='cookie/media', null=True, blank=True, verbose_name='Фото для слайдера')
    description = models.TextField(max_length=210, null=True, verbose_name='Описание')
    alter_descript = models.TextField(max_length=100, null=True, verbose_name='Краткое описание в каталоге')
    price = models.FloatField(default=0, verbose_name='Цена')
    weight = models.IntegerField(default=0, verbose_name='грамм в упаковке')
    date_upload = models.DateTimeField(default=timezone.now(), verbose_name='Дата загрузки')
    display = models.BooleanField(default=False, verbose_name='Показывать')
    hit = models.BooleanField(default=False, verbose_name='Хит недели')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    uuid = models.CharField(max_length=36)
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Имя')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')
    address = models.CharField(max_length=250, null=True, blank=True, verbose_name='Адрес')
    sum = models.FloatField(null=True, blank=True, verbose_name='Сумма заказа')
    date_upload = models.DateTimeField(default=timezone.now(), verbose_name='Дата оформления')
    closed = models.BooleanField(default=False, verbose_name='Заказ закрыт')

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.sum)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderElem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='Продукт')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, verbose_name='Заказ')
    count = models.IntegerField(null=True, verbose_name='Вес')
    sum = models.FloatField(default=0, verbose_name='Сумма')

    @property
    def sum(self):
        return self.count * self.product.price

    def add_total_sum(self):
        self.order.sum += self.order.sum + self.sum

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'


class PhotoProduct(models.Model):
    photo = models.ImageField(upload_to='cookie/media', verbose_name='Фото')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='Продукт')
    main = models.BooleanField(default=False, verbose_name='Главная')

    class Meta:
        verbose_name = 'Фото продкта'
        verbose_name_plural = 'Фото продукта'


class Call(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Имя')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')
    address = models.CharField(max_length=250, null=True, blank=True, verbose_name='Адрес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ звонка'
        verbose_name_plural = 'Заказы звонка'
