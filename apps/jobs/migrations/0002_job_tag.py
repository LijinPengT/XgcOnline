# Generated by Django 2.1.5 on 2019-03-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='tag',
            field=models.CharField(default='', max_length=100, verbose_name='岗位标签'),
        ),
    ]