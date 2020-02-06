from django.db import models
from django.utils import timezone


# Create your models here.
class BoardModel(models.Model):
    # 記事
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True,blank=True,default=0)
    read = models.IntegerField(null=True,blank=True,default=0)
    readtext = models.CharField(max_length=200,null=True,blank=True,default='a')
    created_date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Comment(models.Model):
    # コメント
    name=models.CharField(max_length=100,blank=True,default='名無し')
    text=models.TextField()
    post=models.ForeignKey(BoardModel,on_delete=models.CASCADE)
    created_date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class Reply(models.Model):
    # 返信コメント
    name=models.CharField(max_length=100,blank=True)
    text=models.TextField()
    target=models.ForeignKey(Comment,on_delete=models.CASCADE)
    is_publoc=models.BooleanField(default=True)
    created_date=models.DateTimeField(default=timezone.now)
    # defaultの値をFalseにしておくと、コメントの承認機能をつけることが出来る
    # Trueなので、承認機能が無い状態
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()


class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
            (STATUS_DRAFT, "下書き"),
            (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)