from django.shortcuts import render
from django.views import View
from finance.forms import RegisterForm

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'finance/register.html', {'form':form})