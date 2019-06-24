from django.db import models

# Create your models here.
class bookUser(models.Model):
    userName=models.CharField('用户名',max_length=100,default='no_name')
    password=models.CharField('密码',max_length=100,default='123456')
    bookrack=models.CharField('书架',max_length=200,default='')

    def __str__(self):
        # return '%d: %s' % (self.pk, self.userName)
        return self.userName