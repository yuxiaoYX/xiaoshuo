# Generated by Django 2.2.1 on 2019-06-26 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190626_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksearch',
            name='requests_data',
            field=models.CharField(max_length=100, verbose_name='post访问数据'),
        ),
        migrations.AlterField(
            model_name='booksearch',
            name='requests_url',
            field=models.CharField(max_length=100, verbose_name='网址'),
        ),
        migrations.AlterField(
            model_name='booksearch',
            name='search_key',
            field=models.TextField(verbose_name='源搜索键'),
        ),
        migrations.AlterField(
            model_name='booksearch',
            name='search_value',
            field=models.TextField(verbose_name='源搜索值'),
        ),
        migrations.AlterField(
            model_name='booksearch',
            name='source_name',
            field=models.CharField(max_length=30, verbose_name='源名称'),
        ),
    ]
