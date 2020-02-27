# XgcOnline

## 系统概述
+ 系统具有完整的用户登录注册以及找回密码功能，拥有完整个人中心。
+ 个人中心: 修改头像，修改密码，修改邮箱，可以看到我的岗位以及我的收藏。可以删除收藏，我的消息。
+ 导航栏: 岗位中心，授课讲师，全局搜索。
+ 点击岗位申请–> 岗位列表，排序-搜索。岗位的分页
+ 点击公开课–> 课程列表，排序-搜索。热门课程推荐，课程的分页。
+ 点击课程–> 课程详情页中对课程进行收藏，取消收藏。富文本展示课程内容。
+ 点击开始学习–> 课程的章节信息，课程的评论信息。课程资源的下载链接。
+ 点击授课讲师–>授课讲师列表页，对讲师进行人气排序以及分页，右边有讲师排行榜。
+ 点击讲师的详情页面–> 对讲师进行收藏和分享，以及讲师的全部课程。
+ 后台管理系统可以切换主题。左侧每一个功能都有列表显示, 增删改查，筛选功能。
+ 岗位列表页、课程列表页可以对不同字段进行排序。选择多条记录进行删除操作。
+ 岗位列表页、课程列表页：过滤器->选择字段范围等,搜索,导出csv，xml，json。
+ 岗位新增页面上传图片，富文本的编辑，到岗日期，薪资选择。
+ 课程新增页面上传图片，富文本的编辑。时间选择，添加章节，添加课程资源。
+ 日志记录：记录后台人员的操作

## 项目依赖

+ Package                Version
+ ---------------------- --------
+ defusedxml             0.5.0
+ diff-match-patch       201811116
+ Django                 2.1.5
+ django-crispy-forms    1.7.2
+ django-formtools       2.1
+ django-import-export   1.2.0
+ django-pure-pagination 0.3.0
+ django-ranged-response 0.2.0
+ django-reversion       3.0.3
+ django-simple-captcha  0.5.6
+ DjangoUeditor          1.8.143
+ et-xmlfile             1.0.1
+ future                 0.17.1
+ httplib2               0.9.2
+ jdcal                  1.4
+ mysqlclient            1.4.1
+ odfpy                  1.4.0
+ openpyxl               2.5.14
+ Pillow                 5.4.1
+ pip                    19.0.1
+ pytz                   2018.9
+ PyYAML                 3.13
+ setuptools             40.8.0
+ six                    1.12.0
+ tablib                 0.12.1
+ unicodecsv             0.14.1
+ wheel                  0.32.3
+ xlrd                   1.2.0
+ xlwt                   1.3.0

### 进入虚拟环境workon xxx
+ 安装mkvirtualenv
+ pip install xxx
