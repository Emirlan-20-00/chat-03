from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'user', UserProFileViewSet, basename='user_list')
router.register(r'follow', FollowViewSet, basename='follow_list')
router.register(r'post-like', PostLikeViewSet, basename='post_like_list')
router.register(r'comment', CommentViewSet, basename='comment_list')
router.register(r'comment_like', CommentLikeViewSet, basename='comment_like_list')
router.register(r'story', StoryViewSet, basename='story_list')
router.register(r'save', SaveViewSet)
router.register(r'saveItem', SaveItemViewSet)


urlpatterns = [
     path('', include(router.urls)),
     path('post/', PostListApiView.as_view(), name='post_list'),

     path('register/', RegisterView.as_view(), name='register'),
     path('login/', CustomLoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),

]
