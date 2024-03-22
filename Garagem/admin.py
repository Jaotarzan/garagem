from django.contrib import admin
from .models import Categoria, Marca

# Register your models here.
admin.site.register(Marca)
admin.site.register(Categoria)