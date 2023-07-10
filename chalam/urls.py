from django.urls import path

from chalam.views import *

app_name='chalam'

urlpatterns=[
    path('mam/',mam,name='mam'),
    path('sravani/',sravani,name='sravani'),
]