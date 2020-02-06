from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import CreateView,View
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseNotFound

import django_filters
from rest_framework import viewsets, filters

from .models import BoardModel, Comment, Reply

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer



class FailedRequest(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(status=400)

        return response


def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')


class CommentView(CreateView):
    model = Comment
    fields = ('name', 'text')
    template_name = 'comment_form.html'

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(BoardModel, pk=post_pk)

        comment = form.save(commit=False)
        comment.post = post
        # comment.post = get_object_or_404(BoardModel, pk=post_pk)
        comment.save()
        # 記事の設定

        return redirect('detail', pk=post_pk)
        # 記事の詳細にリダイレクト


class ReplyView(CreateView):
    model = Reply
    fields = ('name', 'text')
    template_name = 'comment_form.html'

    def form_valid(self, form):
        comment_pk = self.kwargs['pk']
        comment = get_object_or_404(BoardModel, pk=comment_pk)

        reply = form.save(commit=False)
        reply.target = comment
        reply.save()
        # 記事の設定

        return redirect('detail', pk=comment.target.pk)
        # 記事の詳細にリダイレクト
