from django import forms
from .models import User
from .models import Momotaro

class UserCreateForm(forms.ModelForm):
    accept_check = forms.BooleanField()
    class Meta:
        model = User
        fields = ('nickname', 'gender', 'age','email', 'additional_comments', 'password')

class MomotaroCreateForm(forms.ModelForm):
    class Meta:
        model = Momotaro
        fields = ('goal', 'limit', 'reason', 'additional_comments')
