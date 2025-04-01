from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('packages/', views.packages, name='packages'),
    path('dashboard/<int:id>', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_reg, name='register'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('details/<str:pName>', views.details, name='details'),
    path('booking/<str:pName>', views.booking, name='booking'),
    path('cancel/<int:id>', views.cancel, name='cancel'),

]