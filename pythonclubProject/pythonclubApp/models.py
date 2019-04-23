from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.DateTimeField()
    location=models.TextField(null=True, blank=True)
    agenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle

class MeetingMinutes(models.Model):
    
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.meetingid

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    URL=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourcename

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.DateTimeField()
    description=models.TextField(null=True, blank=True)
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle