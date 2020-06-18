# importing stuff
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

# get the usermanager
from .managers import UserManager

# The Basic User Class
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('Full Name'), max_length=25)
    email = models.EmailField(_('Email Address'), unique=True)
    is_applicant = models.BooleanField(_('Applicant'), default=False)
    is_admin = models.BooleanField(_('kkk Admin'), default=False)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def clean(self):
        super().clean() 
        self.email = self.__class__.objects.normalize_email(self.email)

# We'll have job opening for different Teams in the KKK. Declaratory class for that.
class Team(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name_plural = "Teams"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)   


# Declartory class for a single Applicant
GENDERS = (('MALE', 'male'), ('FEMALE', 'female'))
AGE = (('kiddo', 'Kiddo'), ('teen', 'Teenager'), ('legal', 'Legal'), ('mid-life crisis', 'Mid-Life Crisis'), ('boomer', 'Boomer'))
class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preference = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDERS, null=True, blank=True)
    locn = models.CharField(_('What do you call home Comrade ?'), max_length=20, null=True, blank=True)
    desc = models.TextField(_("Why do you want to join The Resistance Fighting Force ? "), blank=False, null=True)
    app_type = models.CharField("What type of applicant are you ?", max_length=20, choices=AGE, null=True, blank=True)

    def __str__(self):
        return self.user.name
