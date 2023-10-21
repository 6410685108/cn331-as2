from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUser , ListRegSubject
from subjects.models import subject

class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(username='testuser', email='test@example.com', phone='1234567890')
        subject.objects.create(subjectID='SUB123', subjectName='Test Subject', remaining_class=10, max_class=20, subjectStatus=True)
        ListRegSubject.objects.create(user=CustomUser.objects.get(username='testuser'), Subject=subject.objects.get(subjectID='SUB123'))

    def test_custom_user_fields(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.phone, '1234567890')

    def test_list_reg_subject_fields(self):
        list_reg_subject = ListRegSubject.objects.get(id=1)
        self.assertEqual(list_reg_subject.user.username, 'testuser')
        self.assertEqual(list_reg_subject.Subject.subjectID, 'SUB123')

class UserProfileEditTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password'
        )

    def test_user_profile_edit_view(self):
        self.client.login(username='testuser', password='password')

        edit_profile_url = reverse('edit_profile')

        updated_user_data = {
            'first_name': 'Updated First Name',
            'last_name': 'Updated Last Name',
            'email': 'updated@example.com',
            'phone': '9876543210',
        }

        response = self.client.post(edit_profile_url, updated_user_data)

        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('profile'))

        updated_user = CustomUser.objects.get(username='testuser')

        self.assertEqual(updated_user.first_name, 'Updated First Name')
        self.assertEqual(updated_user.last_name, 'Updated Last Name')
        self.assertEqual(updated_user.email, 'updated@example.com')
        self.assertEqual(updated_user.phone, '9876543210')

class RegisterTest(TestCase):
    def setUp(self):
        self.test_subject = subject.objects.create(subjectID='TEST123', subjectName='Test Subject', remaining_class=10, max_class=20, subjectStatus=True)

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password'
        )

    def test_user_register_subject(self):
        self.client.login(username='testuser', password='password')

        register_url = reverse('register', args=[self.test_subject.subjectID])

        response = self.client.get(register_url)

        updated_subject = subject.objects.get(subjectID=self.test_subject.subjectID)
        self.assertEqual(updated_subject.remaining_class, 9)

    def test_user_unregister_subject(self):
        test_subject = subject.objects.create(subjectID='TEST456', subjectName='Test Subject 2', remaining_class=5, max_class=20, subjectStatus=True)

        ListRegSubject.objects.create(user=self.user, Subject=test_subject)

        self.client.login(username='testuser', password='password')

        unregister_url = reverse('unregisted', args=[test_subject.subjectID])

        response = self.client.get(unregister_url)

        updated_subject = subject.objects.get(subjectID=test_subject.subjectID)
        self.assertEqual(updated_subject.remaining_class, 6)
