from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='cookie/media', verbose_name='Фото', null=True)
    description = models.TextField(null=True, verbose_name='Описание')
    display = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    photo_for_slider = models.ImageField(upload_to='cookie/media', null=True, blank=True)
    description = models.TextField(null=True)
    alter_descript = models.TextField(null=True)
    price = models.FloatField(default=0)
    date_upload = models.DateTimeField(default=timezone.now())
    display = models.BooleanField(default=False)
    hit = models.BooleanField(default=False)
    for_main = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    uuid = models.CharField(max_length=36)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    sum = models.FloatField(null=True, blank=True)
    date_upload = models.DateTimeField(default=timezone.now())
    closed = models.BooleanField(default=False)

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.sum)


class OrderElem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    weight = models.FloatField(null=True)
    sum = models.FloatField(default=0)
    include = models.BooleanField(default=True)

    @property
    def sum(self):
        return self.weight * self.product.price

    def add_total_sum(self):
        self.order.sum += self.order.sum + self.sum


class PhotoProduct(models.Model):
    photo = models.ImageField(upload_to='cookie/media', verbose_name='Фото')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    main = models.BooleanField(default=False)
