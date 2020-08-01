from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length = 300)
    buy_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    sell_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    producer = models.CharField(max_length = 100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Stock(models.Model):
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE)   
    quantity = models.IntegerField
    date = models.DateField()

    def __str__(self):
        return self.Item.name

