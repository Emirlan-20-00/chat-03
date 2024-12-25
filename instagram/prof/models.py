from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProFile(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Follow(models.Model):
    follower = models.ForeignKey(UserProFile, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(UserProFile, on_delete=models.CASCADE, related_name='followings')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower}, {self.following}'


class Post(models.Model):
    user = models.ForeignKey(UserProFile, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post_image/', null=True, blank=True)
    video = models.FileField(upload_to='post_video', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    hashtag = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class PostLike(models.Model):
    user = models.ForeignKey(UserProFile, on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user}, {self.post}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(UserProFile, on_delete=models.CASCADE, related_name='user_comment')
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post}, {self.user}'


class CommentLike(models.Model):
    user = models.ForeignKey(UserProFile, on_delete=models.CASCADE, related_name='comment_likes')
    comment_like = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_c')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment_like')

    def __str__(self):
        return f'{self.user}, {self.comment}'


class Story(models.Model):
    user = models.ForeignKey(UserProFile, on_delete=models.CASCADE, related_name='stories')
    image = models.ImageField(upload_to='stories_image', null=True, blank=True)
    video = models.FileField(upload_to='stories_video', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class Save(models.Model):
    save_user = models.OneToOneField(UserProFile, on_delete=models.CASCADE, related_name='saves')

    def __str__(self):
        return f'{self.save_user}'


class SaveItem(models.Model):
    post_item = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='save_items')
    save_item = models.ForeignKey(Save, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post_item}'


class Chat(models.Model):
    person = models.ManyToManyField(UserProFile)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProFile, on_delete=models.CASCADE)
    chat_text = models.TextField()
    image = models.ImageField(upload_to='chat/image/', null=True, blank=True)
    video = models.FileField(upload_to='chat/video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
