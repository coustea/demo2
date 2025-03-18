from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField('序号',primary_key=True)
    username = models.CharField('用户名',max_length=64)
    password = models.CharField('密码',max_length=64)
    email = models.CharField('邮箱',max_length=64)

    class Meta:
        db_table = 'users'