from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    RegSubject_set = models.ManyToManyField(to='subjects.subject', through='users.ListRegSubject',related_name='StudentReg_set')
    
class ListRegSubject(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='list_subject')
    Subject = models.ForeignKey('subjects.subject', on_delete=models.CASCADE, related_name='list_name')
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'Subject'], name='unique_user_subject'
            )
        ]
    
    def __str__(self) -> str:
        return f'{self.user}-{self.Subject}'