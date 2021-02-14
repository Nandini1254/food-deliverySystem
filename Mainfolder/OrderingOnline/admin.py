from django.contrib import admin

# Register your models here.
from .models import user,Order,Item,Category
admin.site.register(user)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Order)