from django.conf.urls import url, include

from . import views

app_name = 'cookie'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^catalog/(?P<category_id>[0-9]+)/$', views.catalog, name='catalog'),
    url(r'^catalog/product/(?P<product_id>[0-9]+)/$', views.product_detail, name='product'),
    url(r'^basket/$', views.basket, name='basket'),
    #url(r'^search/', include('haystack.urls')),
    url(r'^search/$', views.search, name='search'),
]