from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FinanciadorViewSet, AreaTecnologicaViewSet, ColaboradorViewSet, ProjetoViewSet
)

router = DefaultRouter()
router.register(r'financiadores', FinanciadorViewSet)
router.register(r'areas-tecnologicas', AreaTecnologicaViewSet)
router.register(r'colaboradores', ColaboradorViewSet)
router.register(r'projetos', ProjetoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
