# Generated by Django 2.1.5 on 2019-02-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_courseorg_catgory'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='课程数'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='students',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
    ]
