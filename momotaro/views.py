from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserCreateForm, MomotaroCreateForm
from .forms import MomotaroCreateForm
from .models import User


# Create your views here.
from django.http import HttpResponse

def index(request):
    """TOPページ"""
    return render(request, 'momotaro/index.html')


def about(request):
    """Aboutページ"""
    return render(request, 'momotaro/about.html')


"""ユーザー登録"""
class UserIndexView(generic.ListView):
    model = User
    success_url = reverse_lazy('momotaro:index')

class UserAddView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('momotaro:index')

class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = "momotaro/user_update.html"
    success_url = reverse_lazy('momotaro:index')

class UserDeleteView(generic.DeleteView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('momotaro:index')

class UserDetailView(generic.DetailView):
    model = User


"""桃太郎登録"""
def momotarocreateform(request):
    """桃太郎登録ページへ"""


    context = {
        "user_form": UserCreateForm,
        "momotaro_form": MomotaroCreateForm,
    }
    return render(request, 'momotaro/momotaro_form.html', context)
