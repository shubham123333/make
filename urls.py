from django.contrib import admin
from django.urls import path
from mi import views

urlpatterns = [
    path('contact',views.contact),

    path('',views.make,name='make'),
    path('submit',views.submit , name='submit'),
    path('about',views.about,name='about'),
    path('signin',views.sign,name='sign')
]