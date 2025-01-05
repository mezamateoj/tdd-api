from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from recipes import models
from recipes import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe API"""

    serializer_class = serializers.RecipeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Recipe.objects.all()

    def get_queryset(self):
        """Retireve recipes for auth user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')