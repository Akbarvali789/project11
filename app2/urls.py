from django.urls import path
from app2.views import *
app_name='rolex'
urlpatterns=[
    path('okjanu/',okjanu,name='okjanu'),
    path('raabta/',raabta,name='raabta')
]