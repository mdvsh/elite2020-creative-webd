from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Applicant
from captcha.fields import ReCaptchaField
from django.core import validators
from django.core.exceptions import ValidationError

User = get_user_model()

class ApplicantRegForm(forms.ModelForm):
    password1 = forms.CharField(label="Enter Password", required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password.", required=True, widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('name', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('The passwords you entered are not the same')
        return password1
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        foo = User.objects.filter(email=email)
        if foo.exists():raise ValidationError("The provided email already exists in the Database.")
        return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_applicant = True
        user.save()
        applicant = Applicant.objects.create(user=user)
        return user


class ApplicantForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    
    class Meta:
        model = Applicant
        fields = ('dob', 'locn', 'gender', 'desc', 'app_type')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=144, widget=forms.EmailInput(attrs={'autofocus': True}))

# For the admin dashboard stuff
class AdminUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Enter Password", required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password.", required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('name', 'email',)

    def clean_password2(self):
        data = self.cleaned_data
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('The passwords you entered are not the same')
        return password1
        
    # Function to save the user once the passwords match, also hash the passwords
    def save(self, commit=True):
        # save hashed password
        user = super(ApplicantRegForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:user.save()
        return user


class AdminUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'is_active', 'is_superuser',)

    def clean_password(self):
        """
        No matter what the user provides, return the initial value. This is done here, rather than on the field, 
        because the field does not have access to the initial value.
        """
        return self.initial["password"]