from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from ckeditor.fields import RichTextField

from accounts.models import Applicant, Team
User = settings.AUTH_USER_MODEL

# Create your models here.
WORK_TYPES = (('Full-Time', 'fulltime'), ('Internship', 'internship'))
AGE = (('kiddo', 'Kiddo'), ('Teen', 'Teenager'), ('Legal', 'Legal'), ('Mid-life crisis', 'Mid-Life Crisis'), ('Boomer', 'boomer'))
STATUS = (('Applied', 'applied'), ('Shorlisted', 'shortlisted'), ('Accepted', 'accepted'), ('Rejected', 'rejected'))

# The Job Model (VIMP!!! jk)
class Job(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)
    work_type = models.CharField('Opening Type.', max_length=10, choices=WORK_TYPES)
    age = models.CharField('Required candidate\'s age.', max_length=20, choices=AGE, null=True, blank=True)
    pay = models.PositiveIntegerField(blank=True, null=True)
    desc = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        function to get the absolute job opening urlm useful for the listing
        """
        return reverse('job', kwargs={'slug':self.slug})

class JobApplicationManager(models.Manager):
    """
    handle application process, restricting multiple application and preventing admin job apply
    params
    apld : application accept boolean
    prompt : message to accompany action
    used in views.py in ApplyJob view to validate form
    """
    def alrd_applied(self, user, job):
        apld = False
        prompt = "So you Choose Resistance!! Your Application for joining The RFF has been Recieved."
        if user.is_applicant:
            applicant = user.applicant
            query_set = self.get_queryset().filter(job=job, applicant=applicant)
            if query_set.exists():
                apld = True
                prompt = "Arre Bro Bro... You've already applied for this job."
        else:
            prompt = "Bro tu swayam Bhagwan (Admin) hai! Why apply job eh ?"
        return apld, prompt


# also store job application resumes locally (nice to have them you know)
# resume stored in media(MEDIA_ROOT)/job_app_res/user_{id}/{fname}
def res_store_dir_path(instance, fname):
    return 'job_apps_res/user_{0}/{1}'.format(instance.applicant.user.id, fname)


class JobApplication(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True, null=False)
    date_apld = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default="applied")
    resume = models.FileField(upload_to=res_store_dir_path, null=True)
    objects = JobApplicationManager()
    
    def __str__(self):
        return self.applicant.user.name
    