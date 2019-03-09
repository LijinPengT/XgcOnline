# -*- coding: utf-8 -*-
__author__ = 'Dwyane'
__date__ = '2019/2/15 17:38'
from django.urls import path, include, re_path

from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView
from .views import MyCourseView, MyFavTeacherView, MyFavCourseView, MyMessageView, MyJobView
# MyFavOrgView

app_name = 'users'

urlpatterns = [
    path('info/', UserInfoView.as_view(), name="user_info"),

    # 用户上传/修改头像
    path('image/upload/', UploadImageView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    path('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),

    # 发送邮箱验证码
    path('sendemail_code/', SendEmailCodeView.as_view(), name="sendemail_code"),

    # 用户个人中心修改邮箱
    path('update_email/', UpdateEmailView.as_view(), name="update_email"),

    # 用户课程
    path('mycourse/', MyCourseView.as_view(), name="mycourse"),

    # 用户岗位
    path('myjob/', MyJobView.as_view(), name="myjob"),

    # 我收藏的课程机构
    # path('myfav/org/', MyFavOrgView.as_view(), name="myfav_org"),

    # 我收藏的授课讲师
    path('myfav/teacher/', MyFavTeacherView.as_view(), name="myfav_teacher"),

    # 我收藏的课程
    path('myfav/course/', MyFavCourseView.as_view(), name="myfav_course"),

    # 我的消息
    path('my_message/', MyMessageView.as_view(), name="my_message")

]