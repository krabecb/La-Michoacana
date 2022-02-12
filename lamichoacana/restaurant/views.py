from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

# Create your views here.
def index(request):
    queryset = Item.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'menu.html', context)