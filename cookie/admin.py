from django.contrib import admin
from .models import Product, Category, Order, OrderElem, PhotoProduct, Call


class PhotoProductInline(admin.TabularInline):
    model = PhotoProduct


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name']
    search_fields = ['name']
    inlines = (PhotoProductInline,)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderElem)
admin.site.register(PhotoProduct)
admin.site.register(Call)

