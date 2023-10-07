from django.contrib import admin
from .models import subject

# Register your models here.
class adminsubject(admin.ModelAdmin):
    list_display = ['subjectName', 'subjectID', 'remaining_class', 'max_class', 'subjectStatus']
    search_fields = ['subjectName']
    list_filter = ['subjectStatus']


admin.site.register(subject, adminsubject)