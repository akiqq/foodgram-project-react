from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from recipes.models import Cart, Favorite, Ingredient, Recipe, Tag
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly
from .serializers import (IngredientSerializer, RecipeGetSerializer,
                          RecipePostDeleteSerializer, RecipeSerializer,
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
    permission_classes = (IsAuthorOrReadOnly, )
    serializer_class = RecipeGetSerializer
    queryset = Recipe.objects.select_related(
        'author').prefetch_related(
        'ingredients', 'tags')
    pagination_class = None

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RecipeGetSerializer
        return RecipePostDeleteSerializer

    @action(
        detail=True,
        methods=('post', 'delete'),
        permission_classes=[IsAuthenticated]
    )
    def favorite(self, request, **kwargs):
        recipe = get_object_or_404(Recipe, id=kwargs['pk'])

        if request.method == 'POST':
            serializer = RecipeSerializer(
                recipe, data=request.data, context={"request": request}
            )
            serializer.is_valid(raise_exception=True)
            if not Favorite.objects.filter(
                user=request.user, recipe=recipe
            ).exists():
                Favorite.objects.create(user=request.user, recipe=recipe)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                {'error': 'Рецепт уже в избранном.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.method == 'DELETE':
            get_object_or_404(
                Favorite, user=request.user, recipe=recipe
            ).delete()
            return Response(
                {'detail': 'Рецепт успешно удален из избранного.'},
                status=status.HTTP_204_NO_CONTENT
            )

    @action(
        detail=True,
        methods=('post', 'delete'),
        permission_classes=(IsAuthenticated,),
        pagination_class=None
    )
    def shopping_cart(self, request, **kwargs):
        recipe = get_object_or_404(Recipe, id=kwargs['pk'])

        if request.method == 'POST':
            serializer = RecipeSerializer(
                recipe, data=request.data, context={"request": request}
            )
            serializer.is_valid(raise_exception=True)
            if not Cart.objects.filter(
                user=request.user, recipe=recipe
            ).exists():
                Cart.objects.create(user=request.user, recipe=recipe)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.method == 'DELETE':
            get_object_or_404(Cart, user=request.user, recipe=recipe).delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAuthenticated]
    )
    def download_shopping_cart(self, request, **kwargs):
        ingredients = (
            Ingredient.objects.filter(
                recipe__shopping_recipe__user=request.user
            ).values('ingredient').annotate(
                total_amount=Sum('amount')
            ).values_list(
                'ingredient__name',
                'total_amount',
                'ingredient__measurement_unit'
            )
        )

        file_list = []
        for ingredient in ingredients:
            file_list.append('{} - {} {}.'.format(*ingredient))

        file = HttpResponse(
            'Cписок покупок:\n' + '\n'.join(file_list),
            content_type='text/plain'
        )
        FILE_NAME = 'cart_list.txt'
        file['Content-Disposition'] = (f'attachment; filename={FILE_NAME}')

        return file
