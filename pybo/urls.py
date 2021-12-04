from django.urls import path

from . import views

app_name='pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/create/', views.contact_create, name='contact_create'),
]