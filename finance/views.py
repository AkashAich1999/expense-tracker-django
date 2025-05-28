from django.shortcuts import render, HttpResponse
from django.views import View

# Function Based View.
def Home(request):
    return HttpResponse("<h1>Hello Django !</h1>")

# Class Based View.
# HomeView inherits from View class
# This allows us to handle different HTTP methods (GET, POST, etc.) as separate methods in the class.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello Django Class !</h1>")
    
# Class Based View with Template.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'finance/home.html')