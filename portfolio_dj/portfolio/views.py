from django.shortcuts import render
from django.http import HttpResponse

def home(request): 
    # return HttpResponse("hello Jiocoders! Home view that returns a simple greeting.")
    return render(request, 'portfolio.html')  # Render the home template

def contact(request): 
    return HttpResponse("hello Jiocoders! Contact view that returns a simple greeting.")

def about(request): 
    return HttpResponse("hello Jiocoders! About view that returns a simple greeting.")
