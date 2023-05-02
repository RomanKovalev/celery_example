Deployed here: http://5.249.155.170:8002/

How to use post scheduling.
1. Login to admin part http://5.249.155.170:8002/admin
2. admin:ZBiPm1RSig7Zm
3. Go to admin/quotes/post/ and choose any post.
4. Uncheck "Featured QOTD" and uncheck "Featured QOTD"
5. Choose date and time in field "Published" . I reccomend use something in the nearest future (in a 1-2 minutes, for example).
6. Save post.
7. Go to the main page and check when chosen post will be set up as featured and appear on the mainpage.
8. Congrates. Celery is configured, up and running.


Used tech stack. 
Main stack is Django, django-crispy-forms.

The project is opensource but my parts are:
Celery tasks, wrapping up in the Docker-Compose, Github actions as CD.

DEPRECATED
1. Install Redis in the OS.
- Via Brew: https://medium.com/@petehouston/install-and-config-redis-on-mac-os-x-via-homebrew-eb8df9a4f298
or
- As Docker container: https://hub.docker.com/_/redis
Check if it runs: sudo systemctl status redis

2. Create virtualenv for Django and then activate it (select Python 3.6+ version):
virtualenv -p python3.7 venv

3. Install pip dependencies:
pip install -r requirements.txt

4. Run in the new console celery from the project directory: celery -A bonfire_quotes worker -B -l INFO

Logic.
Begin conditions: no any post with feature_qotd = True and featured_as_qotd = True. Some posts has published field in the future.
Celery task checks every "schedule" seconds if any post published__lte=datetime.now() and feature_qotd = False and featured_as_qotd = False.
If exists, get the nearest to the NOW moment.
	Change of all featured posts.
	Change post's feature_qotd to the True.
If not exists do nothing.

You can find "schedule" time parameter in the settings.CELERY_BEAT_SCHEDULE dictionary.
schedule: 10 - for example, equals task runs every 10 seconds, you may change as you want (in seconds).

/admin/quotes/post/ 
You can find here filter at the right. If you clicked Scheldued, you'll see all posts which are scheduled. All equals see all posts.


So i understand that we have different environments and ready to help with solve.
Sometimes redis install can be a little challenging :)
Send me console output with error and description of the problem if you need help.