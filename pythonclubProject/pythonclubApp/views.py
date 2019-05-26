from django.shortcuts import render, get_object_or_404
from .models import Meeting,MeetingMinutes,Resource,Event
from .forms import ResourceForm
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'pythonclubApp/meetingdetail.html',{'meet': meet})  

@login_required
def newResource(request):
    form=ResourceForm
    if request.method=='POST':
         form=ResourceForm(request.POST)
         if form.is_valid():
             post=form.save(commit=True)
             post.save()
             form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'pythonclubApp/newresource.html', {'form':form})  

@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
         form=MeetingForm(request.POST)
         if form.is_valid():
             post=form.save(commit=True)
             post.save()
             form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'pythonclubApp/newmeeting.html', {'form':form})  

def loginmessage(request):
    return render(request,'pythonclubApp/loginmessage.html')

def logoutmessage(request):
    return render(request,'pythonclubApp/logoutmessage.html')