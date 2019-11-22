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
        # Do we have post to set as featured
        post = Post.objects.filter(
        published__lte=datetime.now(), 
        feature_qotd = False,
        featured_as_qotd = False
        ).order_by('-published').first()

        if (post):
            # if we have post to feature, remove feature mark on featuring now posts
            # and set mark "featured_as_qotd"
            try:
                feature_qotd_post = Post.objects.get(feature_qotd = True)
                feature_qotd_post.feature_qotd = False
                feature_qotd_post.featured_as_qotd = True
                feature_qotd_post.save()
            except:
                pass
            finally:
                # set "post" as featured
                post.feature_qotd = True
                post.save()
    except Exception as e:
        print(e)
