from django import forms
from .models import apply, Job


class applyform(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['name', 'email', 'web', 'cv', 'cover']


class addform(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug', 'owner')
