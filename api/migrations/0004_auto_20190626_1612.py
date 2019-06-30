# Generated by Django 2.2.1 on 2019-06-26 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190626_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksearch',
            name='requests_charset',
            field=models.CharField(default='utf-8', max_length=200, verbose_name='网站编码'),
        ),
        migrations.AlterField(
            model_name='booksearch',
            name='requests_data',
            field=models.CharField(default='', max_length=10, verbose_name='post访问数据'),
        ),
        migrations.AlterField(
            model_name='booksearch',
            name='requests_method',
            field=models.CharField(default='post', max_length=10, verbose_name='访问方式post或get'),
        ),
        migrations.AlterField(
            model_name='booksearch',
            name='requests_url',
            field=models.CharField(default='', max_length=100, verbose_name='网址'),
        ),
        migrations.AlterField(
            model_name='booksearch',
            name='search_key',
            field=models.CharField(default='', max_length=100, verbose_name='源搜索键'),
        ),
        migrations.AlterField(
            model_name='booksearch',
            name='search_value',
            field=models.CharField(default='', max_length=100, verbose_name='源搜索键'),
        ),
        migrations.AlterField(
            model_name='booksearch',
            name='source_name',
            field=models.CharField(default='', max_length=30, verbose_name='源名称'),
        ),
    ]