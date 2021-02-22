from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json
from db import writeDB, readDB, findDB

DB=settings.DB
# Create your views here.
def reg(request):
    if request.method =="GET":
        return HttpResponse("<h1> nothing to get here</h1>")


    
    elif request.method =="POST":
        data_obj=json.loads(request.body)
        if data_obj['add']=='true':
            user_obj=data_obj['dat']
            if findDB(user_obj)==False:
                writeDB(obj=user_obj,loc='userdata')
                if findDB(user_obj)==True:
                    return JsonResponse({"regStatus":"success"})
            else:return JsonResponse({"regStatus":"fail"})

    else:return HttpResponse("<h1> not a method</h1>")

def log_in(request):

    if request.method == "POST":
        inobj=json.loads(request.body)
        if inobj['add']=='false':
            
            if findDB(inobj['dat'])==True:
                return JsonResponse({"logStatus":True})
            else:return JsonResponse({"logStatus":False})
        else:return JsonResponse({"logStatus":False})
        

    elif request.method =="GET":
        return HttpResponse("<h1> nothing to get here</h1>")

    else:return HttpResponse("<h1> not a method</h1>")

def get_catalog(request):
    if request.method =="GET":
        return JsonResponse(readDB(loc='sitedata'))

    elif request.method =="POST":
        return HttpResponse("<h1> need to code for posting in catalog (with ID verification )</h1>")

    else:return HttpResponse("<h1> not a method</h1>")



