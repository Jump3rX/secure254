from .models import Report
from django.forms import ModelForm
from django import forms

class ReportForm(ModelForm):
    class  Meta:
        model = Report
        fields = '__all__'
        exclude = ['verified','latitude','longitude'] #Fields from the model that will not be included in form

        widgets = {
            #adding class and placeholder attributes to the form inputs.
            'county':forms.Select(attrs={'class':'form-control'}),
            'area':forms.TextInput(attrs={'class':'form-control'}),
            'incident':forms.Select(attrs={'class':'form-control'}),
            'occurence_date':forms.TextInput(attrs={'class':'form-control'}),
            'Describe_other_incident':forms.Textarea(attrs={'class':'form-control','placeholder':'Describe only of incident is selected as other.'}),
        }