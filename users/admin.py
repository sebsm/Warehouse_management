from django.contrib import admin
from .models import Customer, Courier, Employee, HR, Manager
# Courier, Employee, HR, Manager
# Register your models here.
admin.site.register(Customer)
admin.site.register(HR)
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(Courier)