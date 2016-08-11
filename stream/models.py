from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.
class StreamEvent(models.Model):
    # "title"
    what = models.CharField(max_length=255)
    # Longer description
    whatwhat = models.TextField()
    # "link"
    where = models.URLField()
    when = models.DateTimeField()
    # Assuming only users can trigger events
    who = models.ForeignKey(AUTH_USER_MODEL)
