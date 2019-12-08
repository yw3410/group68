from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
import random

from .models import Sighting

class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'

def sighting_list(request, template_name='sightings/list.html'):
    sightings = Sighting.objects.all()
    context = {
            'sightings' : sightings,
    }
    return render(request, template_name, context)

def sighting_add(request, template_name='sightings/add.html'):
    form = SightingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sighting_list')
    return render(request, template_name, {'form':form})

def sighting_update(request, pk, template_name='sightings/update.html'):
    sighting = get_object_or_404(Sighting, pk=pk)
    form = SightingForm(request.POST or None, instance=sighting)
    if request.method=='POST' and 'update' in request.POST:
        if form.is_valid():
            form.save()
            return redirect('sighting_list')
    if request.method=='POST' and 'delete' in request.POST:
        sighting.delete()
        return redirect('sighting_list')
    return render(request, template_name, {'form':form})

def sighting_stats(request,template_name='sightings/stats.html'):
    all_count = Sighting.objects.all().count()
    adult_count = Sighting.objects.filter(age='Adult').count()
    juvenile_count = Sighting.objects.filter(age='Juvenile').count()
    running = Sighting.objects.filter(running=True).count()
    chasing = Sighting.objects.filter(chasing=True).count()
    climbing = Sighting.objects.filter(climbing=True).count()
    eating = Sighting.objects.filter(eating=True).count()
    foraging = Sighting.objects.filter(foraging=True).count()

    context = {
            'all_count' : all_count,
            'adult_count': adult_count,
            'juvenile_count': juvenile_count,
            'running' : running,
            'chasing' : chasing,
            'climbing' : climbing,
            'eating' : eating,
            'foraging' : foraging,
            }
    return render(request, template_name, context)

# Create your views here.
