# -*- coding: utf-8 -*-
__author__ = 'Dwyane'
__date__ = '2019/3/8 19:56'
from django.urls import path, re_path

from .views import JobListView, JobDetailView, JobInfoView

app_name = "jobs"
urlpatterns = [
    # 课程列表页
    path('list/', JobListView.as_view(), name="job_list"),
    re_path(r'^detail/(?P<job_id>\d+)', JobDetailView.as_view(), name="job_detail"),
    re_path(r'^info/(?P<job_id>\d+)', JobInfoView.as_view(), name="job_info")
]
