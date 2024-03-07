from django.contrib import admin

# Register your models here.
from .models import Customer, Seller, Product

admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Product)