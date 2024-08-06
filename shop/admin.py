from django.contrib import admin
from .models import Contact, Place_Orders, OrderUpdate, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Place_Orders)
admin.site.register(OrderUpdate)
