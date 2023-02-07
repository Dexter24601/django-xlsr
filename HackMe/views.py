from django.shortcuts import render
import os

# Create your views here.


def index(request):
    os.system('start cmd /k "cd/ & tree" ')
    return render(request,'./index.html')
