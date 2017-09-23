# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
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

# get_list_or_404 shortcut use Product.objects.filter() instead of Product.objects.get()
# return 404 if get an empty list
def filtrados(request):
	productos = get_list_or_404(Product, name="Cichle")
	return render(request, "products/index.html", {"products" : productos})	

# def index(request):
# 	lista_productos = Product.objects.all()
# 	template = loader.get_template("products/index.html")
# 	context = {
# 		"products" : lista_productos
# 	}
# 	return HttpResponse(template.render(context, request))

#get_object_or_404 shortcut
def detail(request, product_id):
	producto = get_object_or_404(Product, pk=product_id)
	return render(request, "products/detail.html", {"producto" : producto})	

# def detail(request, product_id):	
# 	try:
# 		producto = Product.objects.get(pk=product_id)
# 	except Product.DoesNotExist:
# 		raise Http404("El producto no existe.")
# 	return render(request, "products/detail.html", {"producto" : producto})	

def ubicaciones(request, product_id):
	product = "Estas buscando las ubicaciones del producto %s."
	return HttpResponse(product % product_id)

def votar(request, product_id):
	product = "Estas votando por el producto %s."
	return HttpResponse(product % product_id)