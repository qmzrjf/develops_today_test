from django.contrib import admin
from blog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    fields = ["title", "author", "votes", "link"]


class CommentAdmin(admin.ModelAdmin):
    fields = ["post", "author", "content"]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
