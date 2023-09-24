from django.contrib import admin
from .models import subject

# Register your models here.
class adminsubject(admin.ModelAdmin):
    list_display = []


admin.site.register(subject)