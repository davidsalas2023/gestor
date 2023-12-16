from django.urls import path,include
from Usuarios import views

urlpatterns = [
    ######Maneja el inicio de sesion
    path('accounts/', include('django.contrib.auth.urls')),
    #####
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    #Modulo Parking
    path('estacionamiento/<str:token>/', views.estacionamiento, name='estacionamiento'),
    path('estacionamiento/<str:token>/Datos', views.listaautos, name='lista'),
    path('eliminarautosf/<str:patente>',views.eliminarautosf),
    path('editarautosf/<str:patente>',views.editarautosf),


    #Url Administracion
    path('administracion/<str:token>/', views.estacionamiento, name='administracion'),
    path('administracion/<str:token>/Datos', views.listaautos, name='lista.perso'),
    path('eliminarpersonasf/<str:patente>',views.eliminarautosf),
    path('editarpersonasf/<str:patente>',views.editarautosf),
    #Url admin
    path('admin/<str:token>/', views.estacionamiento, name='admin'),
    path('admin/<str:token>/Datos', views.listaautos, name='perso'),
  


]
