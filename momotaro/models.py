from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    nickname = models.CharField('ニックネーム',max_length=100 ,null=False)
    gender = models.CharField('性別', max_length=10 ,null=True)
    age = models.CharField('年齢', max_length=3 ,null=True)
    email = models.EmailField('メールアドレス' ,null=True)
    additional_comments = models.TextField('自由記入欄', max_length=500 ,null=True)
    password = models.CharField('パスワード', max_length=30 ,null=True)
    date = models.DateTimeField('作成日',default=timezone.now)

class Momotaro(models.Model):
    goal = models.CharField('目標', max_length=255 ,null=False)
    limit = models.CharField('期限', max_length=20 ,null=False)
    reason = models.CharField('目標を設定した理由', max_length=255 ,null=True)
    additional_comments =  models.TextField('自由記入欄', max_length=500 ,null=True)
    date = models.DateTimeField('作成日', default=timezone.now)
