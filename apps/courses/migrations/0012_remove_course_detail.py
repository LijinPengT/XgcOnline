# Generated by Django 2.1.5 on 2019-03-01 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_bannercourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='detail',
        ),
    ]
