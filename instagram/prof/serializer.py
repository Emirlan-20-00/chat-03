from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProFile
        fields = ('username', 'email', 'password', 'last_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProFile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProFile
        fields = '__all__'


class UserProFileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProFile
        fields = ['first_name']


class FollowSerializer(serializers.ModelSerializer):
    follower = UserProFileReviewSerializer(read_only=True)
    following = UserProFileReviewSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    user = UserProFileReviewSerializer(read_only=True)
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Post
        fields = ['id', 'user', 'image', 'video', 'description', 'hashtag', 'created_at']


class PostLikeSerializer(serializers.ModelSerializer):
    user = UserProFileReviewSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = PostLike
        fields = ['id', 'user', 'post', 'like', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    user = UserProFileSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    parent = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), write_only=True)
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'text', 'parent', 'created_at']


class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserProFileReviewSerializer(read_only=True)
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), write_only=True)
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = CommentLike
        fields = ['id', 'user', 'comment', 'like', 'created_at']


class StorySerializer(serializers.ModelSerializer):
    user = UserProFileReviewSerializer(read_only=True)
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Story
        fields = ['id', 'user', 'image', 'video', 'created_at']


class SaveItemSerializer(serializers.ModelSerializer):
    post_item = PostSerializer(read_only=True)
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = SaveItem
        fields = ['id', 'post_item', 'created_at']


class SaveSerializer(serializers.ModelSerializer):
    items = SaveItemSerializer(many=True, read_only=True)

    class Meta:
        model = Save
        fields = ['id', 'save_user', 'items']
