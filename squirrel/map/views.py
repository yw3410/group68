from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from sightings.models import Sighting

def sighting_map(request, template_name='map/map.html'):
    sightings = Sighting.objects.order_by('?')[:100]
    context = {
            'sightings' : sightings,
    }
    return render(request, template_name, context)

# Create your views here.
