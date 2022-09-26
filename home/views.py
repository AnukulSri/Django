from multiprocessing import context
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index (request):
    context = {
        "variable1":"Hi how are you",
        "variable2":"what are you doing"        
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
    # return HttpResponse("THIS IS about page ")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services ")
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        Password=request.POST.get('Password')

        contact = Contact(name=name,email=email,message=message,Password=Password,date=datetime.today())
        contact.save()
        messages.success(request, 'Message has been send!')
    
    return render(request,'contact.html')
    # return HttpResponse("this is contact Page ")