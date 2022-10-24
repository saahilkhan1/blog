

from django.urls import path
from . import views

urlpatterns = [
    path('base',views.Base,name='base'),
    path('home',views.Home,name='home'),
    path('',views.Login,name='login')

]

