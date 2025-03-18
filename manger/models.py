from django.db import models

# Create your models here.

class Manger(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'manger'