from django.urls import path

from main.apps import MainConfig
from main.views import PostCreateAPIView, PostListAPIView, PostRetrieveAPIView, PostUpdateAPIView, \
    PostDestroyAPIView, CommentsCreateAPIView, CommentsListAPIView, CommentsRetrieveAPIView, \
    CommentsUpdateAPIView, CommentsDestroyAPIView

app_name = MainConfig.name

urlpatterns = [
    path('post/create/', PostCreateAPIView.as_view(), name='post_create'),
    path('post/list/', PostListAPIView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostRetrieveAPIView.as_view(), name='post_get'),
    path('post/update/<int:pk>/', PostUpdateAPIView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDestroyAPIView.as_view(), name='post_delete'),

    path('comments/create/', CommentsCreateAPIView.as_view(), name='comments_create'),
    path('comments/list/', CommentsListAPIView.as_view(), name='comments_list'),
    path('comments/<int:pk>/', CommentsRetrieveAPIView.as_view(), name='comments_get'),
    path('comments/update/<int:pk>/', CommentsUpdateAPIView.as_view(), name='comments_update'),
    path('comments/delete/<int:pk>/', CommentsDestroyAPIView.as_view(), name='comments_delete'),
]
