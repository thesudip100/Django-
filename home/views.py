from django.shortcuts import render
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    # return HttpResponse("This is the homepage")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("This is 'about' page")
    return render(request,'about.html')

def services(request):
    # return HttpResponse("This is 'services' page")
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact_obj=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact_obj.save()
    # return HttpResponse("This is 'contact' page")
    return render(request,'contact.html')

