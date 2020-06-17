from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Applicant, Department
from .forms import AdminUserCreationForm, AdminUserChangeForm 
# Register your models here.

# modifying UserAdmin for when admin changes some stuff
class UserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    form_tba = AdminUserCreationForm
    # displaying stuff
    list_display = ('email', 'is_superuser')
    fieldsets = ((None, {'fields': ('name', 'email', 'password')}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),)
    # UserAdmin is overriding add_fieldsets to use this attribute when creating a user.
    add_fieldsets = ((None, {'classes': ('wide',),'fields': ('email', 'password1', 'password2')}),)
    ordering = ('email',)
    search_fields = ('email',)
    filter_horizontal = ()

# register models for the admin dashboard
admin.site.register(User, UserAdmin)
# It's not needed actually
# admin.site.unregister(Group)
admin.site.register(Applicant)
admin.site.register(Department)
