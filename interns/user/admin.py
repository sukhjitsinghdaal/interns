from django.contrib import admin

# Register your models here.

from .models import User,ProjectUser


admin.site.register(ProjectUser)
admin.site.register(User)
