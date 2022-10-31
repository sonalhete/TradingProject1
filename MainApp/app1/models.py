from django.db import models

# Create your models here.
class Bank(models.Model):
    ID = models.IntegerField(('ID'),max_length=50),
    OPEN=models.CharField(('OPEN'),max_length=100),
    HIGH=models.CharField(('HIGH'),max_length=150),
    LOW=models.CharField(('LOW'),max_length=200),
    CLOSE=models.CharField(('CLOSE'),max_length=200),
    DATE=models.DateField(('DATE'),auto_now=True)

