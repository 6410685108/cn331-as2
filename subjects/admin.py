from django.contrib import admin
from .models import subject
from users.models import ListRegSubject

class ListRegSubjectInline(admin.TabularInline):  # หรือใช้ StackedInline แทน
    model = ListRegSubject
    extra = 1  # กำหนดจำนวนช่องในแบบฟอร์ม

class adminsubject(admin.ModelAdmin):
    list_display = ['subjectName', 'subjectID', 'remaining_class', 'max_class', 'subjectStatus']
    search_fields = ['subjectName']
    list_filter = ['subjectStatus']
    ordering = ('subjectID',)
    inlines = [ListRegSubjectInline]

admin.site.register(subject, adminsubject)