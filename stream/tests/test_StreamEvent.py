from django.contrib.auth.models import User
from django.test import TestCase
from stream.models import StreamEvent

class StreamEventTestCase(TestCase):
    def test_can_save(self):
        user = User.objects.create_user(username='test', password='test')
        m = StreamEvent(what="Hacked", 
                        whatwhat="This guy hacked the WWW and found KITTENS!",
                        where="http://hacktheplanet.com",
                        when="2016-08-14 18:46-05:00",
                        who=user)
        m.save()
        self.assertIsNotNone(m.id)
