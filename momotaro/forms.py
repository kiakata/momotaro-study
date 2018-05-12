from django import forms
from .models import User
from .models import Momotaro

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nickname', 'email', 'additional_comments')

class MomotaroCreateForm(forms.ModelForm):
    class Meta:
        model = Momotaro
        fields = ('goal', 'limit', 'reason', 'additional_comments')
