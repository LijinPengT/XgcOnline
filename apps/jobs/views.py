# coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
from django.http import HttpResponse
from django.db.models import Q

from .models import Job
from operation.models import UserFavorite, UserJob
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.


class JobListView(View):
    def get(self, request):
        all_job = Job.objects.all().order_by("-add_time")

        hot_jobs = Job.objects.all().order_by("-click_nums")[:3]

        # 岗位搜索
        search_keywords = request.GET.get("keyword", "")
        if search_keywords:
            all_job = all_job.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))

        # 岗位排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "people":
                all_job = all_job.order_by("-people")
            elif sort == "hot":
                hot_jobs = all_job.order_by("-click_nums")

        # 对岗位列表进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_job, 3, request=request)

        jobs = p.page(page)

        return render(request, "job-list.html", {
            "all_job": jobs,
            "sort": sort,
            "hot_jobs": hot_jobs,
        })


class JobDetailView(View):
    """
    岗位详情页
    """
    def get(self, request, job_id):
        job = Job.objects.get(id=int(job_id))

        # 岗位的点击数加一
        job.click_nums += 1
        job.save()
        # has_fav_job = False
       # if request.user.is_authenticated:
        #    if UserFavorite.objects.filter(user=request.user, fav_id=job.id, fav_type=1):
         #       has_fav_job = True

            # if UserFavorite.objects.filter(user=request.user, fav_id=job.course_org.id, fav_type=2):
             #   has_fav_org = True
        # tag = job.tag
        # if tag:
        #    relate_jobs = job.objects.filter(tag=tag)[:2]
        # else:
        #     relate_jobs = []
        return render(request, "job-detail.html", {
            "job": job,
           # "relate_jobs": relate_jobs,
           #  "has_fav_job": has_fav_job,
        })


class JobInfoView(LoginRequiredMixin, View):
    """
    岗位信息
    """
    def get(self, request, job_id):
        job = Job.objects.get(id=job_id)
        job.people += 1
        job.save()

        # 查询用户是否已经有了岗位
        user_jobs = UserJob.objects.filter(user=request.user)
        if not user_jobs:
            user_job = UserJob(user=request.user, job=job)
            user_job.save()

            user_jobs = UserJob.objects.filter(job=job)
            user_ids = [user_job.user.id for user_job in user_jobs]
            all_user_jobs = UserJob.objects.filter(user_id__in=user_ids)

            return render(request, "job-info.html", {
                "job": job,
            })
        else:
            return render(request, 'bankfail.html', {})




