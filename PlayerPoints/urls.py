from django.urls import path
from . import views

urlpatterns = [
    path('name/<str:name>', views.name, name='search by name'),
]