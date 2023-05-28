from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.

def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        contact = Contact(name=name, phone=phone, date=datetime.today())
        contact.save()
        
        
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
