from django import forms


class HelloForm(forms.Form):
    name = forms.CharField(label='이름', max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(label='이메일', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    gender = forms.BooleanField(label='성별', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    age = forms.IntegerField(label='나이', min_value=0, max_value=120, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label='생일', required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
