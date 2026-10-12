from django.shortcuts import render
from datetime import datetime


# equal controller in laravel

def index(request):
    name = 'Ahmad',
    last = 'Qosa'
    id = 20220919
    emill = 'msiswerd15@gmail.com'

    address = 'gaza, palestine'
    birthDate =  datetime(2004, 12, 30)
    context = {
        'firstName':name ,
        'lastName': last,
        'studentId': id,
        'address': address ,   
        'emill' :emill  ,                
        'birthDate':birthDate 
    }
      
    return render(request, 'info.html', context)
# Create your views here.
