# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Welcome to Rent a Room Website! ")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("About Rent a Room.")
    return render(request, 'about.html')
