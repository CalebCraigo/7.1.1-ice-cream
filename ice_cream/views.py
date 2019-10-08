from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Icecream

def index(request, selection=None):

    # ice_cream = Icecream.objects.all()
    # ice_cream = [d['available'] for d in ice_cream]
    # print(ice_cream)
    availability = ['Home','featured','weekly', 'daily', 'seasonal']

    if selection == 'Home':
        ice_cream_list = Icecream.objects.all()

    elif selection == 'featured':
        ice_cream_list = Icecream.objects.filter(featured=True)

    else:
        ice_cream_list = Icecream.objects.filter(available=selection.upper())


    context = {
        'ice_cream_list': ice_cream_list,
        'availability': availability
    }

    return render(request, 'ice_creams/index.html', context)

# def base(request):
#
#     ice_cream_nav = Icecream.objects.all()
#
#     context = {
#         'ice_cream_nav' : ice_cream_nav
#     }
#
#     return render(request, 'ice_creams/base.html', context)
