from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # 특별한 유효성 검사나 조작을 하고 싶을때 사용
    def clean_password2(self):
        cd = self.cleaned_data          # 이값을 반드시 찾아서 사용해야한다.
        if cd['password'] != cd['password2']:
            raise forms.VlidationError('Passwords not matched!')
        return cd['password2']