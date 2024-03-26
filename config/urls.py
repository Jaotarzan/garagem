from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from Garagem.views import AcessorioViewSet, CategoriaViewSet, CorViewSet, MarcaViewSet, VeiculoViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]
