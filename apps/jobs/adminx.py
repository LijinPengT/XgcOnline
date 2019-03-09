# -*- coding: utf-8 -*-
__author__ = 'Dwyane'
__date__ = '2019/3/8 12:50'
import xadmin

from .models import Job

class JobAdmin(object):
    list_display = ['name', 'desc', 'detail', 'do_time', 'people',
                    'image', 'click_nums', 'add_time']
    # 搜索查找
    search_fields = ['name', 'desc', 'detail', 'do_time', 'people',
                     'image', 'click_nums', 'add_time']
    # 过滤器
    list_filter = ['name', 'desc', 'detail', 'do_time', 'people',
                   'image', 'click_nums', 'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['people', 'click_nums']
    list_editable = ['desc', 'detail']
    model_icon = 'fa fa-address-book'

    # style_fields = {"detail": "ueditor"}
    # refresh_times = [3, 5]
    # exclude = ['']

xadmin.site.register(Job, JobAdmin)