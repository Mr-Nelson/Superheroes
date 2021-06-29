from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Superhero
# Create your views here.


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroesapp/index.html', context)

def detail(request, superhero_id):
    specific_superhero = Superhero.objects.filter(pk=superhero_id)
    context = {
        'specific_superhero': specific_superhero
    }
    return render(request, 'superheroesapp/detail.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superherosapp:index'))
    else:
        return render(request, 'superheroes/create.html')