from django.urls import path
from jobs import views

urlpatterns = [
    path('apply/', views.ApplyJob.as_view(), name='job_apply'),
    path('<slug:slug>/', views.JobDetail.as_view(), name='job'),
    path('', views.JobList.as_view(), name='jobs'),
]
