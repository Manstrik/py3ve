from django.test import TestCase

from .models import Frame


# Create your tests here.
class FrameTest(TestCase):
    def setUp(self):
        # self.client = client
        Frame(
            window_width=10,
            window_height=10,
        ).save()
