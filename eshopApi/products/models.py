# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=8, decimal_places=2)	

	def __str__(self):
		return self.name
