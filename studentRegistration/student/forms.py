from .models import student
from django import forms

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('name','gender','fname',
                    'roll','email','phone',
                    'branch','address')
