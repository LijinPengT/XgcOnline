# Generated by Django 2.1.5 on 2019-02-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='全国知名', max_length=10, verbose_name='机构标签'),
        ),
    ]
