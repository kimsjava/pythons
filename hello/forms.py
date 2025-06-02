from django import forms
from .models import Friend

class HelloForm(forms.Form):
    name = forms.CharField(label='이름', max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(label='이메일', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    gender = forms.BooleanField(label='성별', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    age = forms.IntegerField(label='나이', min_value=0, max_value=120, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(
        label='생일',
        required=True,
        input_formats=['%Y-%m-%d', '%Y.%m.%d', '%Y/%m/%d', '%d.%m.%Y', '%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'YYYY-MM-DD'
        })
    )


class FriendForm(forms.ModelForm):
    # birthday 필드를 오버라이드하여 커스텀 위젯과 입력 형식 지정
    birthday = forms.DateField(
        label='생일',
        required=True,
        input_formats=['%Y-%m-%d', '%Y.%m.%d', '%Y/%m/%d', '%d.%m.%Y', '%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'YYYY-MM-DD'
        })
    )
    
    class Meta:
        model = Friend  # 올바른 모델 참조 방식
        fields = ['name', 'mail', 'gender', 'age', 'birthday']