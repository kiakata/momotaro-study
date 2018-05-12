from django.shortcuts import render
from .forms import UserCreateForm
from .forms import MomotaroCreateForm

# Create your views here.
from django.http import HttpResponse

def index(request):
    """TOPページ"""
    return render(request, 'momotaro/index.html')

def about(request):
    """Aboutページ"""
    return render(request, 'momotaro/about.html')

def user(request):
    """ユーザー登録ページ"""
    context = {
    'form': UserCreateForm()
    }
    return render(request, 'momotaro/user_form.html',context)

def momotaro(request):
    """桃太郎登録ページ"""
    context = {
    'form': MomotaroCreateForm()
    }
    return render(request, 'momotaro/momotaro_form.html', context)
