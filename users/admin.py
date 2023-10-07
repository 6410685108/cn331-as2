from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser, ListRegSubject

# Register your models here.

class adminListRegSubject(admin.ModelAdmin):
    list_display = ['user', 'Subject']
    search_fields = ['user__username', 'Subject__subjectName', 'Subject__subjectID']
    
admin.site.register(ListRegSubject, adminListRegSubject)
admin.site.register(CustomUser, UserAdmin)