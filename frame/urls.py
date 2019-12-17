from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('add', views.add, name='add'),
    url('delete', views.delete, name='delete')
]
