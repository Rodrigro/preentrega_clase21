"""preentrega_coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from preentrega_coder.views import saludo, vista_con_template
from products.views import create_shirt, list_shirts, create_shoes, list_shoes, list_result, create_accesories, list_accesories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('vista/', vista_con_template),
    path('create_shirt/', create_shirt),
    path('create_accesories/', create_accesories),
    path('list_accesories/', list_accesories),
    path('list_shirts/', list_shirts),
    path('create_shoes/', create_shoes),
    path('list_shoes/', list_shoes),
    path('list_result/',list_result ),
]
