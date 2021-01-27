from django.urls import path
from . import views

app_name = 'teste'

urlpatterns = [
    path('home/', views.home, name='home')
]