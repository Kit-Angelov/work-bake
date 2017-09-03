from django.db import models
import json
from django.utils import timezone


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
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=250, null=True)
    product_list = models.TextField(null=True)
    sum = models.FloatField(null=True)
    date_upload = models.DateTimeField(default=timezone.now())

    def set_product_list(self, x, y):
        order_dict = {}
        try:
            order_dict = json.loads(self.product_list)
            order_dict[x] = y
        except:
            order_dict = {x: y}
        finally:
            self.product_list = json.dumps(order_dict)

    def get_product_list(self):
        return json.loads(self.product_list)

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.name, self.product_list, self.sum)


class PhotoProduct(models.Model):
    photo = models.ImageField(upload_to='cookie/media', verbose_name='Фото')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    main = models.BooleanField(default=False)
