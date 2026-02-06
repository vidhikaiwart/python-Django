from django.http import HttpResponse
from django.shortcuts import render 




def home(request):
   # return HttpResponse("Hello, welcome to my first Django project!")
    return render(request, 'website/index.html')
def about(request):
    return HttpResponse("This is the about page of my first Django project!")

def contact(request):
    return HttpResponse("Contact us at my contact page.")