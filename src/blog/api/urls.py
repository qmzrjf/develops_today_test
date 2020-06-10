from django.urls import path
from blog.api.views import PostsView, PostView, CommentView, CommentsView, post_upvote

app_name = 'api-blog'
urlpatterns = [
    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/<int:pk>', PostView.as_view(), name='post'),
    path('comments/', CommentsView.as_view(), name='comments'),
    path('comments/<int:pk>', CommentView.as_view(), name='comment'),
    path('post-upvote/<int:pk>', post_upvote, name='post_upvote'),
]
