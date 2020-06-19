from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from notchlistApi.models import Cocktail_Ingredient
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class CocktailIngredientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cocktail_Ingredient
        url = serializers.HyperlinkedIdentityField(
            view_name = 'cocktail_ingredient',
            lookup_field = 'id'
        )
        fields = ('id', 'url', 'cocktail_id', 'ingredient_id')
        # depth = 1
class Cocktail_Ingredients(ViewSet):

    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def create(self, request):
        new_cocktail_ingredient = Cocktail_Ingredient()
        new_cocktail_ingredient.cocktail_id = request.data['cocktail_id']
        new_cocktail_ingredient.ingredient_id = request.data['ingredient_id']
        new_cocktail_ingredient.save()

    
        serializer = CocktailIngredientSerializer(new_cocktail_ingredient, context = {'request': request})

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            cocktail_ingredient = Cocktail_Ingredient.objects.get(pk=pk)
            serializer = CocktailIngredientSerializer(cocktail_ingredient, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        cocktail_ingredient = Cocktail_Ingredient.object.get(pk=pk)
        cocktail_ingredient.cocktail_id = request.data['cocktail_id']
        cocktail_ingredient.ingredient_id = request.data['ingredient_id']
        cocktail_ingredient.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            cocktail_ingredient = Cocktail_Ingredient.objects.get(pk=pk)
            cocktail_ingredient.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Cocktail_Ingredient.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        cocktail_ingredients = Cocktail_Ingredient.objects.all()

        serializer = CocktailIngredientSerializer(
            cocktail_ingredients, many=True, context={'request': request}
        )
        return Response(serializer.data)