from rest_framework import serializers

from .models import BoardModel,Comment,Reply,Entry,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_date', 'tatus', 'author')