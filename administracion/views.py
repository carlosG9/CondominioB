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
    # model = visits
    # template_name = 'administracion/administrador.html'


def residente(request):
    return render(
        request,
        'residente.html',
    )
