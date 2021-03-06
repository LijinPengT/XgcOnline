# Generated by Django 2.1.5 on 2019-03-09 10:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_tag'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0002_auto_20190207_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job', verbose_name='岗位')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户岗位',
                'verbose_name_plural': '用户岗位',
            },
        ),
    ]
