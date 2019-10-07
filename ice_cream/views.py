from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Icecream, Option

#
# def index(request):
#     return HttpResponse('Hello, world.')

def detail(request, ice_cream_id):
    ice_cream = get_object_or_404 (Choice, pk=ice_cream_id)
    context = {'ice_cream': ice-cream}
    return render(request, 'ice_creams/detail.html', context)

#     return HttpResponse("Details for ice_cream #%" % ice_cream_id)
 # Create your views here.

def index(request):
    ice_cream_list = Icecream.objects.all()
    context = {
        'ice_cream_list': ice_cream_list
    }
    return render(request, 'ice_creams/index.html', context)

def results(request, ice_cream_id):
    return HttpResponse("Flavors: %s" % ice_cream_id)
