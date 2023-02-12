from django.urls import path
from . import views

urlpatterns = [
    path('check/<str:plugin>', views.check, name='check key'),
    path('new/<str:qq>/<str:plugin>/<str:length>', views.new, name='generate key'),
    path('bindip/<str:qq>/<str:plugin>/<str:ip>', views.bind, name='bind ip'),
    #path('search/<str:qq>', views.search, name='search key')
]
