from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField('用户名',max_length=14)
    password=models.CharField('密码',max_length=14)
    bookrack=models.TextField('书架',null=True)
    create_time=models.CharField('创建时间',max_length=10)
    # create_time=models.DateTimeField('创建时间',auto_now_add=True)
    token=models.CharField('token验证',max_length=100,null=True)

    def __str__(self):
        return self.username