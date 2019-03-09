# coding=utf-8
from django.db import models

from datetime import datetime

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"岗位名称")
    unit = models.CharField(max_length=200, verbose_name=u"用工单位")
    desc = models.CharField(max_length=300, verbose_name=u"岗位描述")
    price = models.IntegerField(default=0, verbose_name=u"岗位薪资")
    tag = models.CharField(max_length=100, verbose_name=u"岗位标签", default="")
    detail = models.TextField(verbose_name=u'岗位详情', default='')
    people = models.IntegerField(verbose_name=u"报名人数", default=0)
    image = models.ImageField(upload_to="job/%Y/%m", verbose_name=u"封面", max_length=100)
    do_time = models.DateTimeField(default=datetime.now, verbose_name=u"上岗时间")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"工作岗位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



