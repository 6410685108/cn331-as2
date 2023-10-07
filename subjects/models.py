from datetime import datetime
from django.db import models

# Create your models here.
class subject(models.Model):
    subjectID = models.CharField(max_length=6)
    subjectName = models.CharField(max_length=64)
    term = models.IntegerField(default=0)
    year = models.IntegerField(default=datetime.now().year)
    remaining_class = models.IntegerField()
    max_class = models.IntegerField()
    subjectStatus = models.BooleanField(default=False)
   
    def __str__(self) -> str:
        return f"{self.subjectName} ({self.subjectID}) {self.subjectStatus}"
    
    



