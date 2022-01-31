from unicodedata import name
from django import views
from django.urls import path
from . import views
from.views import home, welcome, BeliveoStatus

urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', home, name='home'),
    path('json/', BeliveoStatus.as_view(), name='jsonResponse'),
    path('edicionhome/<nombre>', views.edicionhome), 
    path('editarstatus/', views.editarstatus)
]
