from django.shortcuts import render
from django.http import HttpResponse

from products.models import *
from products.forms import ProductForm

# Create your views here.


def create_shirt(request):
    
    
    
    if request.method == 'GET':
        context = {
            'form': ProductForm()
        }

        return render(request, 'products/create_shirt.html', context=context)

    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Camisetas.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request, 'products/create_shirt.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'products/create_shirt.html', context=context)
        
        
def list_shirts(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Camisetas.objects.filter(name__icontains=search)
    else:
        products = Camisetas.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'products/list_shirts.html', context=context)  


def create_shoes(request):
    
       
    if request.method == 'GET':
        context = {
            'form': ProductForm()
        }

        return render(request, 'products/create_shoes.html', context=context)

    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Calzados.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                size = form.cleaned_data['size'],
                stock=form.cleaned_data['stock'],
                
                
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request, 'products/create_shoes.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'products/create_shoes.html', context=context)     
        
def list_shoes(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Calzados.objects.filter(name__icontains=search)
    else:
        products = Calzados.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'products/list_shoes.html', context=context)          


def list_result(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Camisetas.objects.filter(name__icontains=search)
    else:
        products = Camisetas.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'products/list_result.html', context=context)


def create_accesories(request):
    
       
    if request.method == 'GET':
        context = {
            'form': ProductForm()
        }

        return render(request, 'products/create_accesories.html', context=context)

    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Acesories.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
                
                
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request, 'products/create_accesories.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'products/create_accesories.html', context=context)  
        
        
        
def list_accesories(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Acesories.objects.filter(name__icontains=search)
    else:
        products = Acesories.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'products/list_accesories.html', context=context)          