from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name='sherry george'
    return render(request,'index.html',{'obj':name})
def addition(request):
    x=int(request.GET['num1'])
    y = int(request.GET['num2'])
    result=x+y
    return render(request,'result.html',{'result':result})
