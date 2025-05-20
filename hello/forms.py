from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(label='mail', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label='age', min_value=0, max_value=120, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    
    