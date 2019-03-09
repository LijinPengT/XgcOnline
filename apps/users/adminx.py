# coding=utf-8
__author__ = 'Dwyane'
__date__ = '2019/2/7 13:21'
import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "FlyingStudio后台管理系统"
    site_footer = "中国矿业大学(南湖校区)"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type'] # 搜索查找
    list_filter = ['code', 'email', 'send_type', 'send_time'] # 过滤器
    model_icon = 'fa fa-envelope'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']  # 搜索查找
    list_filter = ['title', 'image', 'url', 'index', 'add_time']  # 过滤器
    model_icon = 'fa fa-film'


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)