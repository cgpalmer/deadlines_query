from django import forms
from .models import Csv

class CsvForm(forms.ModelForm):

    class Meta:
        model = Csv
        exclude = ['activated']