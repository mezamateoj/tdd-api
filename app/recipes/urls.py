

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]