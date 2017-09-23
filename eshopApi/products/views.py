# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

# Create your views here.

from .models import Product

# Metodo usando shortcut render() no requiere loader ni HttpResponse
def index(request):
	lista_productos = Product.objects.all()
	context = {
		"products" : lista_productos
	}
	return render(request, "products/index.html", context)

# def index(request):
# 	lista_productos = Product.objects.all()
# 	template = loader.get_template("products/index.html")
# 	context = {
# 		"products" : lista_productos
# 	}
# 	return HttpResponse(template.render(context, request))

def detail(request, product_id):	
	try:
		producto = Product.objects.get(pk=product_id)
	except Product.DoesNotExist:
		raise Http404("El producto no existe.")
	return render(request, "products/detail.html", {"producto" : producto})	

def ubicaciones(request, product_id):
	product = "Estas buscando las ubicaciones del producto %s."
	return HttpResponse(product % product_id)

def votar(request, product_id):
	product = "Estas votando por el producto %s."
	return HttpResponse(product % product_id)