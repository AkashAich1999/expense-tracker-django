from django.shortcuts import render, HttpResponse

# Function Based View.
def Home(request):
    return HttpResponse("<h1>Hello Django</h1>")