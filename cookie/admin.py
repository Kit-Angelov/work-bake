from django.contrib import admin
from .models import Product, Category, Order, OrderElem, PhotoProduct

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderElem)
admin.site.register(PhotoProduct)

