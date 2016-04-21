from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json

# Create your views here.
def index(request):
    return HttpResponse("What a wonderful world!")
    
def restaurant(request):

    url = 'https://api.locu.com/v1_0/venue/search/?locality=lake%20stevens&api_key=9cec4ffbd2988adb04dfdd6ed07e97278861c476'

    json_obj = urllib2.urlopen(url)

    data = json.load(json_obj)
    
    #data['objects'][2]

    return HttpResponse(json.dumps(data))