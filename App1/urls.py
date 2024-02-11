from django.urls import path
from .views import IndexView, AutorView

urlpatterns = [
    path('', IndexView, name= 'inicio' ),
    path('autor/<int:id>', AutorView, name='autor'),
]