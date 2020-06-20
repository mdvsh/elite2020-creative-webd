from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Job, JobApplication
from .forms import JobApplicationForm
from accounts.mixins import ApplicantRequiredMixin, AdminRequiredMixin

from django.db.models import Q

# Create your views here.
class JobList(ListView):
    model = Job
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        d = []
        dt = Job.objects.all()
        for j in dt:
            d.append(j.team.name)
        ctx['dist_teams'] = list(set(d))
        return ctx

class JobDetail(DetailView):
    model = Job
    template_name = 'jobs/job_info.html'

class CreateJob(AdminRequiredMixin, CreateView):
    model = Job
    fields = ('title', 'team', 'work_type', 'age', 'pay', 'desc',)
    
    def get_context_data(self, **kwargs):
        ctx = super(CreateJob, self).get_context_data(**kwargs)
        ctx['is_create'] = True
        return ctx
    
    def form_valid(self, form):
        return super().form_valid(form)


class UpdateJob(AdminRequiredMixin, UpdateView):
    model = Job
    fields = ('title', 'team', 'work_type', 'age', 'pay', 'desc',)


class DeleteJob(AdminRequiredMixin, DeleteView):
    model = Job
    success_url = reverse_lazy('jobs')

class ApplyJob(ApplicantRequiredMixin, CreateView):
    model = JobApplication
    # form_class = JobApplicationForm
    template_name = 'jobs/job_apply.html'
    fields = ('resume', )

    def get_context_data(self, *args, **kwargs):
        ctx = super(ApplyJob, self).get_context_data(**kwargs)
        job_id = self.request.GET.get('job_id')
        self.job = get_object_or_404(Job, pk=job_id)
        ctx['job'] = self.job   
        return ctx
    
    def form_valid(self, form, **kwargs):
        job_id = self.request.GET.get('job_id')
        job = get_object_or_404(Job, pk=job_id)
        has_apld, prompt = JobApplication.objects.alrd_applied(self.request.user, job)
        if not has_apld:
            applicant = self.request.user.applicant
            form.instance.applicant = applicant
            form.instance.job = job
            form.save()
            messages.success(self.request, prompt)
        else:
            messages.warning(self.request, prompt)
        return redirect('job', job.slug)

class AdminJobs(AdminRequiredMixin, ListView):
    template_name = 'admin_dash/job_list.html'
    def get_queryset(self):
        return Job.objects.all()
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


class AdminJobsDetail(AdminRequiredMixin, DetailView):
    model = Job
    template_name = 'admin_dash/job_info.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        apps = JobApplication.objects.filter(~Q(status='rejected') & ~Q(status='accepted'))
        ctx['applications'] = apps
        return ctx