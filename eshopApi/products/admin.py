# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
	list_display = ("id", "name", "description", "price")
	list_filter = ("name", "description", "price")
