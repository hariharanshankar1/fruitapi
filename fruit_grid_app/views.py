from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import fruit
from django.db.models import Q


# Create your views here.
def index(request):
    obj = fruit.objects.all()
    return render(request, 'index.html', {'fruit': obj})


def search(request):
    result = []
    if request.method == 'GET':
        query = request.GET.get('search')
        result = fruit.objects.filter(
            Q(name__icontains=query) | Q(carbohydrates__icontains=query) | Q(protein__icontains=query) | Q(
                fat__icontains=query) | Q(calories__icontains=query) | Q(sugar__icontains=query))
    return render(request, 'search.html', {'query': query, 'result': result})
