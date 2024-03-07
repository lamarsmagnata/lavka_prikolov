from django.db import models
from .seller import Seller


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
