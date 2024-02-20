from django import forms
from .models import *

class Adharform(forms.ModelForm):
    class Meta:
        model = Adhar
        fields = '__all__'


class Allotform(forms.ModelForm):
    class Meta:
        model = Allot
        fields = '__all__'
