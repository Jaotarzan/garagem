from django.contrib import admin
from .models import Acessório, Categoria, Cor, Marca, Veículo

# Register your models here.
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessório)
admin.site.register(Cor)
admin.site.register(Veículo)