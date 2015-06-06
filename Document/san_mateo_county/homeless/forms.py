from django import forms

from .models import HomelessPeople, Donators


class HomelessPeopleForm(forms.ModelForm):
    class Meta:
        model = HomelessPeople



class DonatorsForm(forms.ModelForm):
    class Meta:
        model = Donators
