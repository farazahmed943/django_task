from multiprocessing import context
from django.shortcuts import render,HttpResponse
import requests
import json

# Create your views here.
# Working on pagination, once done will update on the same repo
def Table(request):
    r = requests.get('https://gorest.co.in/public-api/users')
    data = r.json()
    data = data['data']
    context = {'d' : data}
    return render(request,'base.html',context)

def page1(request):
    r = requests.get('https://gorest.co.in/public-api/users?page=1')
    data = r.json()
    data = data['data']
    context = {'d' : data}
    return render(request,'base.html',context)
