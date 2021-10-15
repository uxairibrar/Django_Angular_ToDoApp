from django.db import models

# Create your models here.

class TODO(models.Model):
    ID = models.AutoField(primary_key=True)
    text = models.CharField(max_length=500)

