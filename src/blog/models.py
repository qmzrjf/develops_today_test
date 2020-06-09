from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    link = models.CharField(default="", max_length=120, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    votes = models.PositiveSmallIntegerField(default=0)
    author = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.title}, {self.link}, {self.created}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comment_post"
    )
    author = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post}, {self.author}"
