from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import markdown
from stream.models import StreamEvent

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class BlogPost(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    md_content = models.TextField()
    html_content = models.TextField(blank=True)
    when = models.DateTimeField(auto_now_add=True)

@receiver(pre_save, sender=BlogPost)
def update_markdown(sender, instance, **kwargs):
    instance.html_content = markdown.markdown(instance.md_content, extensions=['markdown.extensions.codehilite'])

@receiver(post_save, sender=BlogPost)
def create_stream_instance(sender, instance, created, **kwargs):
    if created:
        StreamEvent(content_object=instance).save()
