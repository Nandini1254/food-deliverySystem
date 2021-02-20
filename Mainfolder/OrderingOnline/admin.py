from django.contrib import admin

# Register your models here.
from .models import user,customer
admin.site.register(user)
admin.site.register(customer)