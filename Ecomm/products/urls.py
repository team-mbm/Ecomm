from django.conf.urls import url

from . import views
app_name = 'products'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^index/$', views.index, name='index'),
        url(r'^item/(?P<product_id>[0-9]+)/$', views.description, name='description'),
    ]
