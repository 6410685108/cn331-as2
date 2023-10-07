from django.contrib import admin
from .models import subject

# Register your models here.
class adminsubject(admin.ModelAdmin):
    list_display = ['N_subject', 'sec_subject', 'remaining_class', 'max_class', 'is_open']
    search_fields = ['N_subject']
    list_filter = ['is_open']
    filter_horizontal = ['StudentReg_set']


admin.site.register(subject, adminsubject)