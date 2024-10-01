from django import forms
from .models import Hobby, Interest, Skill

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['name','description']


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['name', 'description']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']
