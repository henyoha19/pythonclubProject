from django.test import TestCase
from django.urls import reverse
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

#tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetMeetingTest(TestCase):
    def setUp(self):
        self.meet=Meeting.objects.create(meetingtitle='memberstraining', meetingdate='2019-05-05',
        meetingtime='2019-06-2019 18:08:00', location="capitalhillseattle", agenda="weeklyprogressreport")

    def test_meeting_detail_sucess(self):
        response=self.client.get(reverse('meetingdetails', args=(self.meet.id,)))
        self.assertEqual(response.status_code, 200)