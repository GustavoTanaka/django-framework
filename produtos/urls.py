from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('lista/', views.lista_produtos, name='lista_produtos')
]
