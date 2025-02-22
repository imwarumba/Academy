#!/ismailmwarumba/bin/env python
from django.urls import path
from bambakofi import views

app_name = 'bambakofi'

urlpatterns = [
    path('',views.index, name='index'),
    path('',views.about, name='about'),
]
