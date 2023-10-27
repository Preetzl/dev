from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

import math
import json
import redis
# Create your views here.

redis_client = redis.StrictRedis(host='redis://:"+REDIS_PASSWORD+"@host.docker.internal:6379/0', port= 6379, db=0)
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
        param = float(param)
        x = 5 - param
        data = {"data":x}  
        
        string = data.get('data')
        key = 'carkey'
        redis_client.set(key, string)
        return JsonResponse({"String gespeichert": x})

def get_string(request):
    key = 'carkey'
    cache = redis_client.get(key)
    
    return JsonResponse({"string": cache})       
        
    
    



        
    
    

    
    


        

        
    
    
    