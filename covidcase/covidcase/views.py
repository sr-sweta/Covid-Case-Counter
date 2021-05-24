from django.shortcuts import render
from .models import Contact



def index(request):
    thank = False
    if request.method=="POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        if request.POST.get('txtvalues'):
            savedata = Contact();
            savedata.symptoms = request.POST.get('txtvalues')
        desc = request.POST.get('desc', '')
        contact = Contact(username=username, email=email, phone=phone, symptoms=savedata.symptoms,  desc=desc)
        contact.save()
        thank = True
    return render(request, 'index.html', {'thank': thank})