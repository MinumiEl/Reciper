from rest_framework import serializers
from recipes.models import Recipes


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipes
        fields = ('categoryType',)


class DishesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipes
        fields = ('id', 'name', 'categoryType')


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipes
        fields = ('id', 'name', 'categoryType', 'recipe')