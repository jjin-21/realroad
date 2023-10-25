from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length=10, label='닉네임')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'nickname',)


class CustomUserChangeForm(UserChangeForm):
    nickname = forms.CharField(max_length=10, label='닉네임')

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'nickname',)

    # 비밀번호 필드를 숨깁니다.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')