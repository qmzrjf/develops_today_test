from celery import shared_task
from blog.models import Post


@shared_task
def upvote_clean():
    Post.objects.all().update(votes=0)
