from django import forms
from .models import UserProfile,Business,NeighbourHood,Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude = ['user']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighbourhood']


class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = ('name', 'location', 'occupants')