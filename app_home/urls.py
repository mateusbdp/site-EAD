from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.chanda_login, name='chanda_login'),
    path('logout/', views.chanda_logout, name='chanda_logout'),

]