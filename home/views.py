from django.shortcuts import render, HttpResponse
from home.models import Contact
import datetime
from django.contrib import messages


# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, number=number,
                          mess=message, date=datetime.datetime.now())
        contact.save()
        messages.success(request, 'Your message have been send!')

    return render(request, 'index.html')
    # return HttpResponse("hello, dev!")


''' def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):

    return render(request, 'contact.html') '''
