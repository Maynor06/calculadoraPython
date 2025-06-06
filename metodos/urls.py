from metodos import views
from django.urls import path

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('biseccion/', views.viewBiseccion, name='biseccion'),
    path('newton/', views.viewNewton, name='newton'),
    path('newtonRaphsonModificado/', views.viewNewtonRaphsonModificado, name='newtonRaphsonModificado'),
]
