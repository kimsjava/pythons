from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='url', required=True, widget=forms.URLInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(label='mail', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label='age', min_value=0, max_value=120, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    d1 = forms.DateField(label='date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    t1 = forms.TimeField(label='time', widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    dt1 = forms.DateTimeField(label='datetime', widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    check = forms.BooleanField(label='check', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    