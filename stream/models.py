from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
import os

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.
class StreamEvent(models.Model):
    """ A StreamEvent should be created when a model is created.
    It sets up a foreign relationship
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    when = models.DateTimeField(auto_now_add=True)

    def get_template(self):
        """ Returns the template name for this object.
        The template expects the object to be named "object"
        """
        return os.path.join(self.content_type.app_label, 'fragments', self.content_type.model) + '.html'
