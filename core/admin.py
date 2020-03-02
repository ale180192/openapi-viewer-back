from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class ApiAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, ApiAdmin)