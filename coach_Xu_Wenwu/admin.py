from django.contrib import admin
from coach_Xu_Wenwu.models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email", "password")

admin.site.register(Users, UsersAdmin)
