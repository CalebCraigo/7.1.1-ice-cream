from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Icecream


def index(request, selection=None):

    # ice_cream = Icecream.objects.all()
    # ice_cream = [d['available'] for d in ice_cream]
    # print(ice_cream)
    availability = ['Home','featured','weekly', 'daily', 'seasonal']

    if selection == None:
        ice_cream_list = Icecream.objects.all()

    elif selection == 'Home':
        ice_cream_list = Icecream.objects.all()

    elif selection == 'featured':
        ice_cream_list = Icecream.objects.filter(featured=True)

    else:
        ice_cream_list = Icecream.objects.filter(available=selection.upper())


    context = {
        'ice_cream_list': ice_cream_list,
        'availability': availability
    }

    return render(request, 'ice_cream/index.html', context)

def results(request, ice_cream_id):
    ice_cream = get_object_or_404(Icecream, pk=ice_cream_id)
    return render(request, 'ice_cream/results.html', {'ice_cream':ice_cream})

def vote(request, ice_cream_id):
    ice_cream = get_object_or_404(Icecream, pk=ice_cream_id)
    # selected_choice = ice_cream.choice_set.get(pk=request.POST['choice'])

    ice_cream.likes += 1
    ice_cream.save()

    return HttpResponseRedirect(reverse('ice_cream:results', args=(ice_cream.id,)))

class CreateView(generic.CreateView):
    model = Icecream
    fields = ['flavor', 'base', 'available', 'featured', 'date_churned',]
    template_name = 'ice_cream/create.html'

def icecream_delete(request, pk):
    ice_cream = get_object_or_404(Icecream, pk=pk)

    # if request.method == 'POST':
    ice_cream.delete()
    return redirect(reverse_lazy('ice_cream:index'))

    # return render(request, 'base.html', {'ice_cream': ice_cream})
