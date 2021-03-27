from django.contrib import admin

# Register your models here.
from .models import Item,Category,Order,Restaurant_manager
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Restaurant_manager)