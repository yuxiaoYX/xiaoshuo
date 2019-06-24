# Generated by Django 2.2.1 on 2019-06-24 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(default='no_name', max_length=100, verbose_name='用户名')),
                ('password', models.CharField(default='123456', max_length=100, verbose_name='密码')),
                ('bookrack', models.CharField(default='', max_length=200, verbose_name='书架')),
            ],
        ),
    ]
