from django.shortcuts import render
from django.views.generic import ListView
from accounts.mixins import AdminRequiredMixin
from jobs.models import Job, JobApplication
# Create your views here.
class AdminHome(AdminRequiredMixin, ListView):
    template_name = "admin_dash/home.html"
    def get_queryset(self):
        return Job.objects.all()
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['num_apps'] = JobApplication.objects.count()
        return ctx