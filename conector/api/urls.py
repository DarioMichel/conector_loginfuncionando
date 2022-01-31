from django.urls import path
from.views import home, welcome, BeliveoStatus

urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', home, name='home'),
    path('json/', BeliveoStatus.as_view(), name='jsonResponse'),
]
