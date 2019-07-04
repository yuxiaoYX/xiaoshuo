# Generated by Django 2.2.1 on 2019-07-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190701_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookintroduce',
            name='requests_url',
            field=models.CharField(default=11111111, max_length=100, verbose_name='网址'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookintroduce',
            name='requests_data',
            field=models.CharField(default='{}', max_length=100, verbose_name='访问数据'),
        ),
    ]