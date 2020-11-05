from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
from .models import visits
from .forms import AdministratorForm


def index(request):
    return render(
        request,
        'index.html',
    )


def administrador(request):
    if request.method == 'POST':
        form = AdministratorForm(request.POST)
        visitas = visits.objects.all()
        if form.is_valid():
            form.save()
        return redirect('admin')
    else:
        form = AdministratorForm()
        visitas = visits.objects.all()
    return render(request, 'administracion/administrador.html', {'form': form, 'visitas': visitas})


def administrador_editar(request, id_visits):

    visitas = visits.objects.get(id=id_visits)
    if request.method == 'GET':
        form = AdministratorForm(instance=visitas)
    else:
        form = AdministratorForm(request.POST, instance=visitas)
        if form.is_valid():
            form.save()
        return redirect('admin')
    return render(request, 'administracion/administrador.html', {'form': form})


def administrador_eliminar(request, id_visits):

    visitas = visits.objects.get(id=id_visits)
    if request.method == 'POST':
        visitas.delete()
        return redirect('admin')
    return render(request, 'administracion/administrador_eliminar.html', {'visitas': visitas})


def residente(request):
    if request.method == 'POST':
        form = AdministratorForm(request.POST)
        visitas = visits.objects.all()
        if form.is_valid():
            form.save()
        return redirect('residente')
    else:
        form = AdministratorForm()
        visitas = visits.objects.all()
    return render(request, 'administracion/residente.html', {'visitas': visitas})
