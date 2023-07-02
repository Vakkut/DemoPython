from django.shortcuts import render
from shop.models import Prodect
from django.db.models import Q


def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Prodect.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request,'search.html', {'query':query,'products':products})