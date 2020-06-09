from rest_framework import generics
from django.db.models import F
from django.http import JsonResponse, HttpResponse

from blog.api.serializers import PostSerializer, CommentSerializer
from blog.models import Post, Comment


class PostsView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def post_upvote(request, pk):
    Post.objects.filter(id=pk).update(votes=F('votes')+1)
    return HttpResponse('Votes was incremented')
