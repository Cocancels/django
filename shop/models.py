from django.db import models

# Create your models here.


class Product(models.Model):
    text = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.text
