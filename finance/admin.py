from django.contrib import admin
from finance.models import Transaction, Goal

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Goal)