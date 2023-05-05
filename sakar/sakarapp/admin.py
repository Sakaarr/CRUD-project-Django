from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)
class UserAdmin(User):
    list_display = ('id', 'name', 'email','password')
