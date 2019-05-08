from django.shortcuts import render, get_object_or_404
from .models import Meeting,MeetingMinutes,Resource,Event
# Create your views here.
def index (request):
    return render(request, 'pythonclubApp/index.html')

def getResources (request):
    resources_list=Resource.objects.all()
    return render(request, 'pythonclubApp/resources.html' ,{'resources_list' : resources_list})

def getMeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'pythonclubApp/meetings.html', {'meetings_list' : meetings_list})  

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    return render(request, 'pythonclubApp/meetingdetail.html')  
