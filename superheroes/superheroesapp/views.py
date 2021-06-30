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
    specific_superhero = Superhero.objects.get(pk=superhero_id)
    context = {
        'specific_superhero': specific_superhero
    }
    return render(request, 'superheroesapp/detail.html', context)

def change(request, superhero_id):
    specific_superhero = Superhero.objects.get(pk=superhero_id)
    context = {
        'specific_superhero': specific_superhero
    }
    if request.method == 'POST':
        change_name = request.POST.get('change_name')
        if change_name == '':
            return change_name
        else:
            return specific_superhero.name
    superhero_id.save()
    if request.method == 'POST':
        change_alter_ego = request.POST.get('change_alter_ego')
        if change_alter_ego == '':
            return change_alter_ego
        else:
            return specific_superhero.alter_ego
    superhero_id.save()
    if request.method == 'POST':
        change_primary_ability = request.POST.get('change_primary_ability')
        if change_primary_ability == '':
            return change_primary_ability
        else:
            return specific_superhero.primary_ability
    superhero_id.save()
    if request.method == 'POST':
        change_secondary_ability = request.POST.get('change_secondary_ability')
        if change_secondary_ability == '':
            return change_secondary_ability
        else:
            return specific_superhero.secondary_ability
    superhero_id.save()
    if request.method == 'POST':
        change_catchphrase = request.POST.get('change_catchphrase')
        if change_catchphrase == '':
            return change_catchphrase
        else:
            return specific_superhero.catchphrase
    superhero_id.save()
        return HttpResponseRedirect(reverse('superheroesapp:detail', context))
    else:
        return render(request, 'superheroesapp/change.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroesapp:index'))
    else:
        return render(request, 'superheroesapp/create.html')

def delete(superhero_id):
    delete_superhero = Superhero.objects.get(pk=superhero_id)
    delete_superhero.delete()
    return HttpResponseRedirect(reverse('superheroesapp:index'))