from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class ApplicantRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return (self.request.user.is_active and self.request.user.is_applicant)

# added mixin to further enable admin to create jobs and other admin stuff
class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return (self.request.user.is_active and self.request.user.is_staff)