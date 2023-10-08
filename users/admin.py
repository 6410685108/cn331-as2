from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser, ListRegSubject

# Register your models here.

class adminListRegSubject(admin.ModelAdmin):
    list_display = ['user', 'Subject']
    search_fields = ['user__username', 'Subject__subjectName', 'Subject__subjectID']

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(ListRegSubject, adminListRegSubject)
admin.site.register(CustomUser, CustomUserAdmin)