from django.urls import path, include
from myapp.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', views.ContactBookViewSet, basename='contactbook')

urlpatterns = [
    path('', include(router.urls))
]
