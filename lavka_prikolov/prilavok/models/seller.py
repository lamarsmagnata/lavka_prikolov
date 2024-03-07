from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.name
