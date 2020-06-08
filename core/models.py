from django.conf import settings
from django.db import models


# Defines the logic of storing and order

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def _str_(self):
        return self.title

class OrderItem(models.Model):  
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

class Order(models.Model): # This is so that we can link the order items to the order. 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def _str_(self):
        return self.title

