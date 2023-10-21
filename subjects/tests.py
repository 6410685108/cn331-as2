from django.test import TestCase
from datetime import datetime
from .models import subject

class SubjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        subject.objects.create(subjectID='TEST01', subjectName='Test Subject', term=1, year=datetime.now().year, remaining_class=5, max_class=10, subjectStatus=True)
    
    def test_subjectID_label(self):
        subject_obj = subject.objects.get(id=1)
        field_label = subject_obj._meta.get_field('subjectID').verbose_name
        self.assertEquals(field_label, 'subjectID')
    
    def test_subjectName_max_length(self):
        subject_obj = subject.objects.get(id=1)
        max_length = subject_obj._meta.get_field('subjectName').max_length
        self.assertEquals(max_length, 64)
    
    def test_subjectStatus_default(self):
        subject_obj = subject.objects.get(id=1)
        default_value = subject_obj._meta.get_field('subjectStatus').default
        self.assertEquals(default_value, False)
    
    def test_subject_str_method(self):
        subject_obj = subject.objects.get(id=1)
        expected_object_name = f"{subject_obj.subjectName} ({subject_obj.subjectID}) {subject_obj.subjectStatus}"
        self.assertEquals(str(subject_obj), expected_object_name)
