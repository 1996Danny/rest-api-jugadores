from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()

# endpint
router.register("jugadores", views.JugadoresViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("admin/", admin.site.urls),
]
