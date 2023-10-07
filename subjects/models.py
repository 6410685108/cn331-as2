from django.db import models

# Create your models here.
class subject(models.Model):
    sec_subject = models.IntegerField()
    N_subject = models.CharField(max_length=64)
    teacher = models.CharField(max_length=60)
    max_class = models.IntegerField()
    remaining_class = models.IntegerField()
    is_open = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.N_subject} ({self.sec_subject}) {self.is_open}"
    
    



