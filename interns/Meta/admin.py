from django.contrib import admin

# Register your models here.
from .models import Category,State,Country
admin.site.register(Category)
admin.site.register(State)
admin.site.register(Country)