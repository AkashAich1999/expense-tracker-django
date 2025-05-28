from django.urls import path, include
from finance.views import Home

urlpatterns = [
    path('', Home, name="home"),
    path('home/', Home, name="home"),
]