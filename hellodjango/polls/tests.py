import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Poll, Choice
from django.core.urlresolvers import reverse

class PollMethodTests(TestCase):
    def test_was_published_recently_with_future_poll(self):
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)

    def test_test(self):
        self.assertEqual(True, True)
        self.assertQuerysetEqual([], [])

class PollViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'no poll')
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

