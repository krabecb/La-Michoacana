from django.db import models

# Create your models here.
class Item(models.Model):
    food_name = models.CharField(max_length=200)
    food_desc = models.CharField(max_length=200)
    food_price = models.CharField(max_length=200)

    def __str__(self):
        return self.food_name