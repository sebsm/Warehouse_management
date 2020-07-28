from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Customer, Courier, Employee, HR, Manager


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.CharField(max_length = 200)
    contact_number = models.IntegerField()
    registered = models.DateField()
    
    def __str__(self):
        return self.user.username

class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    contact_number = models.IntegerField()
    company = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.user.username

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    contact_number = models.IntegerField()
    address = models.CharField(max_length = 200)
    salary = models.DecimalField(max_digits = 5, decimal_places = 2)
    employed_since = models.DateField()

    def __str__(self):
        return self.user.username

class HR(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    contact_number = models.IntegerField()
    salary = models.DecimalField(max_digits = 5, decimal_places = 2)
    address = models.CharField(max_length = 200)
    
    def __str__(self):
        return sel.user.username

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    contact_number = models.IntegerField()
    address = models.CharField(max_length = 200)
    
    def __str__(self):
        return sel.user.username