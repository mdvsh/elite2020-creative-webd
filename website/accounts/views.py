from django.shortcuts import render, reverse, redirect
from django.contrib.auth import login
# Generic views are a blessing inshallah!
from django.views.generic import TemplateView, CreateView, FormView, UpdateView
from django.contrib.auth.views import LoginView
# Verify that the current user is authenticated.
from django.contrib.auth.mixins import LoginRequiredMixin

# Get models, forms and mixins
from .models import Applicant
from .forms import ApplicantRegForm, LoginForm, ApplicantForm
from .mixins import ApplicantRequiredMixin

# Create your views here.
class LoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get_success_url(self):
        """
        mechanism for url redirectiona after succesfull form submission
        """
        ng = self.request.GET.get('next')
        np = self.request.POST.get('next')
        nu = ng or np or None
        if nu is not None:return nu

        # handle login differently for admin and applicants
        if self.request.user.is_staff:
            # to do 
            return '/admin/home/'
        elif self.request.user.is_applicant:
            return '/applicant/home/'
        # if admin (later, staff maybe); redirect to admin dashboard



class ApplicantReg(CreateView):
    model = Applicant
    form_class = ApplicantRegForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        complete_profile = reverse('reg_profile',kwargs={'pk': user.applicant.pk})
        return redirect(complete_profile)


class UpdateApplicant(ApplicantRequiredMixin, UpdateView):
    model = Applicant
    form_class = ApplicantForm
    template_name = 'accounts/reg_complete.html'
    success_url = '/applicant/home'