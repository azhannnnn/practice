from django.urls import path
from .views import *

urlpatterns = [
    
    path('',home,name="home"),
    path('add/',add,name="add"),
    path('allot/',allot,name='allot')
     
]
