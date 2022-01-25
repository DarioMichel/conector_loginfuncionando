from django.urls import path
from.views import home, welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', home, name='home')
]
