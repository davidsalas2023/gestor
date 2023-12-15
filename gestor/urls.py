from django.urls import path,include
from Usuarios import views

urlpatterns = [
    ######Maneja el inicio de sesion
    path('accounts/', include('django.contrib.auth.urls')),
    #####
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('estacionamiento/<str:token>/', views.estacionamiento, name='estacionamiento'),
    path('admin/<str:token>/', views.admin, name='admin'),
    path('administracion/<str:token>/', views.administracion, name='administracion'),
]
