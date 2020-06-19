from django.urls import path
from django.views.generic import TemplateView
from jobs import views as jobviews
from .views import AdminHome

urlpatterns = [
    path('job/delete/<int:pk>/', jobviews.DeleteJob.as_view(extra_context={'title': 'Delete Job'}), name='job_delete'),
    path('job/update/<int:pk>/', jobviews.UpdateJob.as_view(extra_context={'title': 'Update Job'}), name='job_update'),
    path('job/create/', jobviews.CreateJob.as_view(extra_context={'title': 'Create a new Job Opening'}), name='job_create'),
    path('job/<int:pk>', jobviews.AdminJobsDetail.as_view(), name='admin_job_info'),
    path('jobs/', jobviews.AdminJobs.as_view(), name='admin_jobs'),
    path('home/', AdminHome.as_view(), name='admin_home'),
]
