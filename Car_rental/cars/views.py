from django.shortcuts import render
from .models import cars
# Create your views here.
def home(request):
    All_cars=cars.objects.all() 
    return render(request, 'home.html', {'all':All_cars})
