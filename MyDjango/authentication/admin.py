from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)

# from django.contrib.auth.models import User
# from django  import forms
# from django.contrib.auth.forms import ReadOnlyPasswordHashField, \
#     UserCreationForm
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.core.exceptions import ValidationError




#
# class UserCreation(forms.ModelForm):
#     password1 = forms.CharField(label = 'Password',widjet =forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation',
#                                 widjet=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fieds = ('email',)
#
#     def clean_password(self):
#         #Check that the two password entries watch
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise ValidationError('Password dont match')
#         return password2
#
#     def save(self,commit = True):
#         #Save the provided password in hashed format
#         user = super().save(commit = False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#
#
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = User
#         fields = ('email','password','is_active','is_staff')
#
#
# class UserProfileAdmin(BaseUserAdmin):
#
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#
#     list_display = ('email','is_staff')
#     list_filter = ('is_staff',)
#     fieldsets = (
#         (None,{'fields':('email','password')}),
#         ('Permissions',{'fields':('is_staff')}),
#     )
#
#     add_fielsets = (
#         (None,{
#         'classes':('wide',),
#         'fields':('email','password1','password2'),
#     })
#     )
#     seach_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()


# admin.site.register(User)


