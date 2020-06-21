from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView
from accounts.mixins import ApplicantRequiredMixin
from jobs.models import JobApplication
# Create your views here.
User = settings.AUTH_USER_MODEL

class ApplicantHome(ApplicantRequiredMixin, ListView):
    model = JobApplication
    template_name = 'app_profile/home.html'

    def get_queryset(self):
        applicant = self.request.user.applicant
        query_set = JobApplication.objects.filter(applicant=applicant)
        return query_set
    