"""Prices URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from los_precios.prices.views import stores

router = DefaultRouter()
router.register(r'stores', stores.StoreViewSet, basename='stores')


app_name = "prices"
urlpatterns = [
    path('', include(router.urls))
]
