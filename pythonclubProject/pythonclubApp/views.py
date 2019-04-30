from django.shortcuts import render
from .models import Meeting,MeetingMinutes,Resource,Event
# Create your views here.
def index (request):
    return render(request, 'pythonclubApp/index.html')

def getResources (request):
    resources_list=Resource.objects.all()
    return render(request, 'pythonclubApp/resources.html' ,{'resources_list' : resources_list})
    