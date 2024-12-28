from recipes.models import Recipes
from .serializers import CategoriesSerializer, DishesSerializer, RecipeSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view


class Recipe_view(ReadOnlyModelViewSet):
    queryset = Recipes.objects.all()
    print(queryset)
    serializer_class = RecipeSerializer


class Categories_view(ReadOnlyModelViewSet):
    queryset = Recipes.objects.values('categoryType').distinct()  # Извлечение уникальных значений поля
    serializer_class = CategoriesSerializer


@api_view(['GET'])
def dishes_view(request):
    if request.method == 'GET':
        dishes = Recipes.objects.filter(categoryType=request.query_params['category'])
        serializer = DishesSerializer(dishes, many=True)
        return Response(serializer.data)
