# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('process video', views.process_video, name='process_video'),
]
