from django.urls import path
from . import views

urlpatterns = [
    path('', views.pd1, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('client/', views.client, name='client'),
    path('location/', views.location, name='location'),
    path('product/', views.product, name='product'),
    path('teststandard/', views.testStandard, name='testStandard'),
    path('certificate/', views.certificate, name='certificate'),
]
