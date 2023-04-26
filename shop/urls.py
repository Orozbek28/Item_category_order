from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'order', views.OrderViewSet)


urlpatterns = [
    path('www/', include(router.urls))

]
