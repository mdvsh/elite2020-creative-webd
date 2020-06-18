"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from .views import HomePage
from accounts.views import LoginView, ApplicantReg, UpdateApplicant

urlpatterns = [
    path('login/', LoginView.as_view(extra_context={'title': 'Login To Your Account'}), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/applicant/', ApplicantReg.as_view(extra_context={'title': 'Applicant Registration'}), name='applicant_reg'),
    path('reg/profile/<int:pk>/', UpdateApplicant.as_view(extra_context={'title': 'Complete your Applicant Profile'}), name='reg_profile'),
    path('', HomePage.as_view(), name="home"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
