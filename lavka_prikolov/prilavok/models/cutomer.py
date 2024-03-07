from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_lenght=50)
    last_name = models.CharField(max_lenght=50)
    birthday = models.DateField(blank=True, null=True)
    email = models.CharField(max_lenght=150)
    registry_date = models.DateTimeField(auto_now_add=True)