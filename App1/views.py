from django.shortcuts import render, get_object_or_404
from .models import AutorDB, FraseBD

def IndexView(request):
    objeto = AutorDB.objects.all().order_by('-id')
    return render(request, 'index.html', {'objeto': objeto})

def AutorView(request,id):
    autor = get_object_or_404(AutorDB, id=id)
    return render(request, 'autor.html', {'objeto': autor})
