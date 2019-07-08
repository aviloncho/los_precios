"""Products URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from los_precios.products.views import items, brands

router = DefaultRouter()
router.register(r'brands', brands.BrandViewSet, basename='brands')
router.register(r'items', items.ItemViewSet, basename='items')


app_name = "products"
urlpatterns = [
    path('', include(router.urls))
]
