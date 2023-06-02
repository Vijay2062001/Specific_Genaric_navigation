from django.urls import path

from venkat.views import *

app_name='venkat'

urlpatterns=[
    path('mams/',mams,name='mams')
]