from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('html_home/', html_home, name='html_home'),
]
