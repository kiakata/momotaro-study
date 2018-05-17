from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm, MomotaroCreateForm
    )


from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404
from django.shortcuts import redirect, resolve_url
from django.template.loader import get_template
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# Create your views here.
class Top(generic.TemplateView):
    template_name = 'register/top.html'


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'register/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'register/top.html'

User = get_user_model()

class UserCreate(generic.CreateView):
    """ユーザー仮登録"""
    template_name = 'register/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        """仮登録と本登録用メールの発行."""
        # 仮登録と本登録の切り替えは、is_active属性を使うと簡単です。
        # 退会処理も、is_activeをFalseにするだけにしておくと捗ります。
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'uidb64': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
            'token': urlsafe_base64_encode(force_bytes(user.email)).decode('utf-8'),
            'user': user,
        }

        # テンプレートを使ってメールを組み立てる
        subject_template = get_template('register/mail_template/create/subject.txt')
        subject = subject_template.render(context)

        message_template = get_template('register/mail_template/create/message.txt')
        message = message_template.render(context)

        user.email_user(subject, message)  # ユーザーのメール送信メソッド
        return redirect('register:user_create_done')


class UserCreateDone(generic.TemplateView):
    """ユーザー仮登録完了"""
    template_name = 'register/user_create_done.html'


class UserCreateComplete(generic.TemplateView):
    """メール内URLアクセス後のユーザー本登録"""
    template_name = 'register/user_create_complete.html'

    def get(self, request, **kwargs):
        """uid、tokenが正しければ本登録."""
        token = kwargs.get('token')
        uidb64 = kwargs.get('uidb64')
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            email = force_text(urlsafe_base64_decode(token))
            user = User.objects.get(pk=uid, email=email)
            if user.is_active:    # すでにis_activeがTrueなら、処理は必要ないので404
                raise Http404
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            pass
        else:
            user.is_active = True
            user.save()
            return super().get(request, **kwargs)

        raise Http404

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetail(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'register/user_detail.html'


class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'register/user_form.html'

    def get_success_url(self):
        return resolve_url('register:user_detail', pk=self.kwargs['pk'])

def momotaro_create(request, pk):
    user = User.object.get(id=pk)

    # 送信内容をもとにフォームを作る。POSTでなければからのフォーム
    form = MomotaroCreateForm(request.POST or None)
    template_name = 'register/momotaro_form.html'
    # method=POST,つまり送信ボタン押下時、入力内容に誤りがなければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('register:index')
    # 通常時のページアクセスや、入力内容に誤りがあれば、またページを表示
    content = {
    'form': form
    }
    return render(request, 'register/momotaro_form.html', context)
