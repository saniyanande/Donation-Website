from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signup, name='signup'),
    path('register/', views.login, name='login'),
]