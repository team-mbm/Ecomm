from django.conf.urls import url

from . import views
app_name = 'products'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^index/$', views.index, name='index'),
        url(r'^item/(?P<product_id>[0-9]+)/$', views.description, name='description'),
        url(r'^category/(?P<category_name>[\w+\s*\w+]+)/$', views.category_items, name='category'),
        url(r'^shop/$', views.all_products, name='all_products'),
    ]
