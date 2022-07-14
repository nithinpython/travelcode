from django.urls import path
from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('about/',views.about,name='about'),
    # path('add/',views.addition,name='addition')
]
