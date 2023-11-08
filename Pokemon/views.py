from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import pickle
from .models import counter 
from django.conf import settings

import os
import math
import json
import redis
# Create your views here.


redis_client = redis.StrictRedis(host='cache', port= 6379, db=0)
# neuer_eintrag = counter(counter='',counter_id='carkey')
# neuer_eintrag.save()
def Eintrag(request):
    new = counter(counter='0',counter_id='carkey')
    new.save()
    return JsonResponse({"Eintrag": 'neu'})



def counter1(primary_key):
    
    datensatz = counter.objects.get(counter_id=primary_key)
    
    datensatz.counter += 1
    
    datensatz.save()
    return datensatz.counter
    



def Pokemon3D(request):
    if request.method == 'POST':
        print('received request:', request.POST['name'])
    
    return render(request, 'Pokemon_3D_Request.html')

    
def test(request, param):
    
    ipi = int(param)
    
    assert ipi < 5 
    
    if ipi > 3:
        result= "bigger than 3"
    else:
        result= "lower than 3"
         
     
    
    data = {"result": result}
    return JsonResponse(data)

def Taschenrechner(request, param0,string, param1):
    
    try:
        param0 = int(param0)
        param1 = int(param1)
    except ValueError:
        return HttpResponse("Brauchst Zahlen")
    else: 
         if string == '+':
            result = param0 + param1
         elif string == '*':
            result = param0 * param1
         elif string == ':':
             if param1 != 0:
                 result = param0/param1
             else:
                 result = 'kannst nich durch NUll teilen digga'           
         elif string == '-':
            result = param0 - param1
         elif string == '**':
            result = param0**param1
        
        
   
    
         Ausgabe = {"Ausgabe": result}
         return JsonResponse(Ausgabe)
     
     
def string(request,param):
        param = int(param)
        x = 5 - param
        data = {"data":x}
        Zähler = counter1('carkey')
        string = data.get('data') #redis Befehle
        key = 'carkey'
        y = os.environ.get('REDIS_PASSWORD')
        redis_client.set(key, pickle.dumps(string),y)
        return JsonResponse({"String gespeichert": x, "Zähler": Zähler})

def get_string(request):
    key = 'carkey'
    cache = redis_client.get(key)
    cache = pickle.loads(cache)
    
    
    return JsonResponse({"string": cache})

def counter2(request):
    
    #Zähler2= counter1('carkey')
    Zähler2 = counter.objects.get(counter_id='carkey')
    Zähler2 = Zähler2.counter
    
    return JsonResponse({"Zähler": Zähler2})



def enviroment(request):
    y = os.environ.get('SECRET_KEY')
    
    return JsonResponse({"Password": y})

       
        
    
    



        
    
    

    
    


        

        
    
    
    