from django.urls import path
from . import views

#this is a comment
urlpatterns=[
    path('', views.index, name='index'),
    path('getResources/', views.getResources, name='resources'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('newResource/', views.newResource, name='newResource'),
    path('newMeeting/', views.newMeeting, name='newMeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]