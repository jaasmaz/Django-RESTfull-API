from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
# router.register('products', views.ProductViewSet)



# URLConf
urlpatterns = [
path('', include(router.urls))
]
 