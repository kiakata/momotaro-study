from django.urls import path
from . import views

app_name = 'momotaro'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/', views.UserIndexView.as_view(), name='user'),
    path('user/add/', views.UserAddView.as_view(), name='user.add'),
    path('user/update/<int:pk>',views.UserUpdateView.as_view(), name='user.update'),
    path('user/delete/<int:pk>', views.UserDeleteView.as_view(), name='user.delete'),
    path('user/detail/<int:pk>', views.UserDetailView.as_view(), name='user.detail'),
    path('momotaro/', views.momotarocreateform, name='momotaro'),
]
