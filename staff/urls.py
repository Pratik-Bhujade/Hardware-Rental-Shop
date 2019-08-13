from . import views
from django.conf.urls import url,include

urlpatterns = [
    url(r'^insert/',views.insert,name='insert'),
    url(r'^update/(?P<id>[0-9]+)$',views.update,name='update'),
    url(r'^delete/(?P<id>[0-9]+)$',views.delete,name='delete'),
    url(r'^rent/(?P<id>[0-9]+)$',views.rent,name='rent'),
    url(r'^review/',views.review,name='review'),
    url(r'^checkout/',views.checkout,name='checkout')
]
