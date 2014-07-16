from django.contrib import admin
from pyfriend.models import User

class UserAdmin(admin.ModelAdmin):
    List_display=('username','email','password')

admin.site.register(User,UserAdmin)
