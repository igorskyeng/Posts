from datetime import datetime
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from main.models import Post, Comments
from django_filters import rest_framework as rest_filters
from main.paginators import Paginator
from main.permissions import IsOwner, Admin
from main.serliazers import PostSerializers, CommentsSerializers


class PostCreateAPIView(generics.CreateAPIView):
    """
    Создание 'Поста'.
    """
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_post = serializer.save()
        new_post.autor = self.request.user
        new_post.save()


class PostListAPIView(generics.ListAPIView):
    """
    Вывод листа постов.
    """
    serializer_class = PostSerializers
    permission_classes = [AllowAny]
    pagination_class = Paginator
    queryset = Post.objects.all()

    # Фильтр по определенной стране.
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['country']


class PostRetrieveAPIView(generics.RetrieveAPIView):
    """
    Вывод поста.
    """
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class PostUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление поста.
    """
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated & (Admin | IsOwner)]

    def perform_update(self, serializer):
        new_post = serializer.save()
        new_post.date_of_editing = datetime.now()
        new_post.save()


class PostDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление поста.
    """
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated & (Admin | IsOwner)]

    def perform_destroy(self, instance):
        instance.delete()


class CommentsCreateAPIView(generics.CreateAPIView):
    """
    Создание 'Комментария'.
    """
    serializer_class = CommentsSerializers
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_comments = serializer.save()
        new_comments.autor_comment = self.request.user
        new_comments.save()


class CommentsListAPIView(generics.ListAPIView):
    """
    Вывод листа комментариев.
    """
    serializer_class = CommentsSerializers
    permission_classes = [AllowAny]
    queryset = Comments.objects.all()
    pagination_class = Paginator

    # Фильтр по определенной стране.
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['country']


class CommentsRetrieveAPIView(generics.RetrieveAPIView):
    """
    Вывод комментария.
    """
    serializer_class = CommentsSerializers
    queryset = Comments.objects.all()
    permission_classes = [AllowAny]


class CommentsUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление комментария.
    """
    serializer_class = CommentsSerializers
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticated & (Admin | IsOwner)]

    def perform_update(self, serializer):
        new_comments = serializer.save()
        new_comments.date_of_editing = datetime.now()
        new_comments.save()


class CommentsDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление комментария.
    """
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticated & (Admin | IsOwner)]

    def perform_destroy(self, instance):
        instance.delete()
