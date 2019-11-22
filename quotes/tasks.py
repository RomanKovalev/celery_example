# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta, datetime
from time import sleep


from .models import Post


@shared_task
def check_posts():
    try:
        # if(datetime.now()

        
        
        q = Post.objects.filter(feature_qotd=False)[0]
        q.feature_qotd = True
        q.save()
    except Exception as e:
        print(e)


def q():
    post = Post.objects.filter(
        published__lte=datetime.now(), 
        feature_qotd = False,
        featured_as_qotd = False
        ).order_by('-published').first()

    if post:
        print(post)
        feature_qotd_post = Post.objects.get(feature_qotd = True)
        feature_qotd_post.feature_qotd = False
        feature_qotd_post.featured_as_qotd = True
        feature_qotd_post.save()

        post.feature_qotd = True
        post.save()

