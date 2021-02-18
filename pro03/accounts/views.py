from django.shortcuts import render
from .forms import RegisterForm
from config.serializers import RegisterSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():            # 이 과정을 거쳐야 비밀번호가 암호화된 상태로 저장됨
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form':user_form})

class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer