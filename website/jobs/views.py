from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Job, JobApplication
from .forms import JobApplicationForm
from accounts.mixins import ApplicantRequiredMixin, AdminRequiredMixin

# Create your views here.
class JobList(ListView):
    model = Job


class JobDetail(DetailView):
    model = Job
    template_name = 'jobs/job_info.html'


class CreateJob(AdminRequiredMixin, CreateView):
    model = Job
    fields = ('titile', 'team', 'work_type', 'age', 'pay', 'desc',)
    
    def get_context_data(self, **kwargs):
        ctx = super(CreateJob, self).get_context_data(**kwargs)
        ctx['is_create'] = True
        return ctx
    
    def form_valid(self, form):
        return super().form_valid(form)


class UpdateJob(AdminRequiredMixin, UpdateView):
    model = Job
    fields = ('titile', 'team', 'work_type', 'age', 'pay', 'desc',)


class DeleteJob(AdminRequiredMixin, DeleteView):
    model = Job
    success_url = reverse_lazy('jobs')

class ApplyJob(ApplicantRequiredMixin, CreateView):
    model = JobApplication
    form_class = JobApplicationForm
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
            messages.info(self.request, prompt)
        return redirect('job', job.slug)
