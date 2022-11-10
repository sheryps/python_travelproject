from django.shortcuts import render
from . models import Place,Person
# Create your views here.
def index(request):
    obj=Place.objects.all()
    per=Person.objects.all()
    return render(request,'index.html',{'values':obj,'per':per})