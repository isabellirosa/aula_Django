
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from app.views import CategoriaViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]
