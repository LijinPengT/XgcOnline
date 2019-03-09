# -*- coding: utf-8 -*-
__author__ = 'Dwyane'
__date__ = '2019/2/7 14:27'
import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['course_org', 'name', 'desc', 'category', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'image', 'click_nums', 'add_time', 'get_zj_nums', 'go_to']
    # 搜索查找
    search_fields = ['course_org', 'name', 'desc', 'category', 'detail', 'degree', 'learn_times', 'students',
                     'fav_nums', 'image', 'click_nums']
    # 过滤器
    list_filter = ['course_org', 'name', 'desc', 'category', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                   'image', 'click_nums', 'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['fav_nums', 'click_nums']
    list_editable = ['degree', 'desc']
    inlines = [LessonInline, CourseResourceInline]
    model_icon = 'fa fa-address-book'
    # style_fields = {"detail": "ueditor"}
    # refresh_times = [3, 5]
    # exclude = ['']

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org)
            course_org.save()


class BannerCourseAdmin(object):
    list_display = ['course_org', 'name', 'desc', 'category', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time', 'get_zj_nums', 'go_to']
    search_fields = ['course_org', 'name', 'desc', 'category', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    # 搜索查找
    list_filter = ['course_org', 'name', 'desc', 'category', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']  # 过滤器
    ordering = ['-click_nums']
    readonly_fields = ['fav_nums', 'click_nums']
    # exclude = ['']
    inlines = [LessonInline, CourseResourceInline]
    model_icon = 'fa fa-address-book'

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']  # 搜索查找
    list_filter = ['course__name', 'name', 'add_time']  # 过滤器
    model_icon = 'fa fa-fire'


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']  # 搜索查找
    list_filter = ['lesson__name', 'name', 'add_time']  # 过滤器
    model_icon = 'fa fa-video-camera'


class CourseResourceAdmin(object):
    list_display = ['courses', 'name', 'download', 'add_time']
    search_fields = ['courses', 'name', 'download']  # 搜索查找
    list_filter = ['courses__name', 'name', 'download', 'add_time']  # 过滤器
    model_icon = 'fa fa-database'


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
