from django.urls import path, include
from finance.views import Home, HomeView

urlpatterns = [
    path('', Home, name="home"),
    path('home/', Home, name="home"),
    path('ghar/', HomeView.as_view(), name="ghar"),
]