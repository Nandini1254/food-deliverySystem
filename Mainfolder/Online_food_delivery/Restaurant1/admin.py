from django.contrib import admin

# Register your models here.
from .models import demo
admin.site.register(demo)
from .models import Item,Category,Order,restaurant,cart
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(restaurant)
admin.site.register(cart)