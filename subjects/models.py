from django.db import models

# Create your models here.
class subject(models.Model):
    sec_subject = models.IntegerField()
    N_subject = models.CharField(max_length=64)
    teacher = models.CharField(max_length=60)
    max_class = models.IntegerField()
    remaining_class = models.IntegerField()