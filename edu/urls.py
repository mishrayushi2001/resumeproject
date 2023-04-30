from django.urls import path
from . import views

path('skills/',views.skill, name='skill')