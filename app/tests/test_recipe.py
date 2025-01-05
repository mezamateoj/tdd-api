from django.contrib.auth import get_user_model
from django.test import TestCase
from recipes import models
from decimal import Decimal
from django.urls import reverse
from recipes.serializers import RecipeSerializer
from rest_framework.test import APIClient
from rest_framework import status


RECIPES_URL = reverse('recipe:recipe-list')


def create_recipe(user, **params):
    """Create recipe helper"""
    defaults = {
        "title": "Sample recipe title",
        "time_minutes": 22,
        "price": Decimal('5.50'),
        "description":'Sample recipe description',
        "link": "http://example.com/recipe.pdf"
    }

    defaults.update(params)

    recipe = models.Recipe.objects.create(user=user, **defaults)
    return recipe


class RecipeTests(TestCase):


    def test_create_recipe(self):
        """Test creating a recipe"""

        user = get_user_model().objects.create_user(
            "test@example.com",
            'testpass123'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample Recipe',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description'
        )

        self.assertEqual(str(recipe), recipe.title)


class PublicRecipesTests(TestCase):
    """Public recipes endpoints"""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API"""

        res = self.client.get(RECIPES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeTests(TestCase):
    """Test RECIPE API"""
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
               'user@example.com',
               'testpass1234'
           )
        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        create_recipe(user=self.user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPES_URL)
        recipes = models.Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_recipes_limited(self):
        other_user = get_user_model().objects.create_user(
               'user2@example.com',
               'testpass1234'
           )
        create_recipe(user=self.user)
        create_recipe(user=other_user)

        res = self.client.get(RECIPES_URL)
        recipes = models.Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    
