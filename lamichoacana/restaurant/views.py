from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

# Create your views here.
def home(request):
    return render(request, 'home.html')

def menu(request):
    queryset = Item.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'menu.html', context)

def locations(request):
    return render(request, 'locations.html')