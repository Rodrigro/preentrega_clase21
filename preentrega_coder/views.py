from django.http import HttpResponse
from django.shortcuts import render



def saludo(request):
    return HttpResponse('Hola')


def vista_con_template(request):
    return render(request, 'template_base.html', context={})