from django.contrib import admin
from .models import Courier, Empoyee, HR, Manager
# Courier, Employee, HR, Manager
# Register your models here.
admin.site.register(Customer, Courier, Employee, HR, Manager)