from django.urls import include, path
from django.views.generic import TemplateView
from app_profile import views

urlpatterns = [
    path('home/', views.ApplicantHome.as_view(), name='applicant_home'),
]
