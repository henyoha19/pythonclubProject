from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        meet=Meeting(meetingtitle='annualmeeting')
        self.assertEqual(str(meet),meet.meetingtitle)

class MeetingMinutesTest(TestCase):
    def test_string(self):
        minutes=MeetingMinutes(minutestext='memberstrainig')
        self.assertEqual(str(minutes),minutes.minutestext)

class ResourceTest(TestCase):
    def test_string(self):
        source=Resource(resourcename='weeklymembersmeeting')
        self.assertEqual(str(source),source.resourcename)

class EventTest(TestCase):
    def test_string(self):
        evn=Event(eventtitle='weeklymembersmeeting')
        self.assertEqual(str(evn),evn.eventtitle)