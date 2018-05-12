from django.urls import path
from . import views

app_name = 'momotaro'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/', views.user, name='user'),
    path('momotaro/', views.momotaro, name='momotaro'),
]
