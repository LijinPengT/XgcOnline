# coding=utf-8
__author__ = 'Dwyane'
__date__ = '2019/2/7 15:40'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']  # 查找
    list_filter = ['name', 'desc', 'add_time']  # 过滤器
    model_icon = 'fa fa-location-arrow'


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city']  # 查找
    list_filter = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city__name', 'add_time']  # 过滤器
    relfield_style = 'fk-ajax'

    model_icon = 'fa fa-university'


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    ]  # 查找
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                   'add_time']  # 过滤器
    model_icon = 'fa fa-male'


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
