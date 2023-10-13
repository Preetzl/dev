from django.db import models
from datetime import date
# Create your models here.

class Pokemon(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=100) 
    done = models.BooleanField(default=False)
    