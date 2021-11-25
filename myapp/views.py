from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from myapp.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def add_data(request):
    User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        mobile = request.POST['mobile']
        )
    return JsonResponse({'msg':'Data Receive','password':'POssword does not match'})