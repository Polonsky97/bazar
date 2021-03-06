from enum import Flag
from bazar.models import (Post, UserProfile)
from rest_framework import serializers


class PostListSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    creator = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)

    class Meta:
        model = Post
        exclude = ['id', ]


class PostCRUDSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    creator = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)

    class Meta:
        model = Post
        exclude = ['slug', 'date_created', 'id']
