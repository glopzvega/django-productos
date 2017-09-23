
from django.conf.urls import url

from . import views

urlpatterns = [
	# Mostrar Todos ej. /products/
	url(r'^$', views.index, name="index"),
	url(r'^filtrados/$', views.filtrados, name="filtrados"),
	# Mostrar Todos
	url(r'^(?P<product_id>[0-9]+)/$', views.detail, name="detail"),
	url(r'^(?P<product_id>[0-9]+)/ubicaciones/$', views.ubicaciones, name="ubicaciones"),
	url(r'^(?P<product_id>[0-9]+)/votar/$', views.votar, name="votar"),
	
]
