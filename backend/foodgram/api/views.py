from django.db.models import F, Prefetch
from recipes.models import Cart, Favorite, Ingredient, Recipe, Tag
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from users.models import Subscriptions

from .serializers import (IngredientSerializer, RecipeGetSerializer,
                          TagSerializer)


class TagViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = None


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = None


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    permission_classes = [AllowAny]
    serializer_class = IngredientSerializer
    pagination_class = None
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']


class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = RecipeGetSerializer
    queryset = Recipe.objects.select_related(
        'author').prefetch_related(
        'ingredients').prefetch_related(
        'tags').prefetch_related(
        Prefetch('favorite', Favorite.objects.select_related(
        'recipe'))).prefetch_related(
        Prefetch('shopping_recipe', Cart.objects.select_related('recipe')))
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)