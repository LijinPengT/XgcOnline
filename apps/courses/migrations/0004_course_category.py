# Generated by Django 2.1.5 on 2019-02-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='数学', max_length=20, verbose_name='课程类别'),
        ),
    ]
