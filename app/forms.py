from django import forms
from django.forms import ModelForm, Textarea

from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_picture']

class ServiceForm(forms.ModelForm):
    class Meta:
        model=Service
        fields='__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }