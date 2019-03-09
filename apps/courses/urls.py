# -*- coding: utf-8 -*-
__author__ = 'Dwyane'
__date__ = '2019/2/15 17:38'
from django.urls import path, re_path

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddComentsView, VideoPlayView


app_name = "courses"
urlpatterns = [
    # 课程列表页
    path('list/', CourseListView.as_view(), name="list"),
    re_path(r'^detail/(?P<course_id>\d+)', CourseDetailView.as_view(), name="course_detail"),
    re_path(r'^info/(?P<course_id>\d+)', CourseInfoView.as_view(), name="course_info"),

    # 课程评论
    re_path(r'^comment/(?P<course_id>\d+)', CommentsView.as_view(), name="course_comments"),

    # 添加课程评论
    re_path(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),

    # 课程视频播放
    re_path(r'^video/(?P<video_id>\d+)', VideoPlayView.as_view(), name="video_play"),

]
