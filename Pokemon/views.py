from django.shortcuts import render



# Create your views here.
def Pokemon3D(request):
    if request.method == 'POST':
        print('received request:', request.POST['name'])
    
    return render(request, 'Pokemon_3D_Request.html')
