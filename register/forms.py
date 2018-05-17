from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,UserCreationForm
)
from django.contrib.auth import get_user_model
from .models import Momotaro


User = get_user_model()


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        fields = ('email', 'nickname')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class UserUpdateForm(forms.ModelForm):
    """ユーザー情報更新フォーム"""

    class Meta:
        model = User
        fields = ('nickname', 'age', 'gender', 'address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

########## 桃太郎登録 #############
class MomotaroCreateForm(forms.ModelForm):
    """桃太郎登録フォーム"""

    class Meta:
        model = Momotaro
        fields = ('goal', 'limit', 'reason', 'additional_comments')
