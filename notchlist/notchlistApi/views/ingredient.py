from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from notchlistApi.models import Ingredient
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class IngredientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingredient
        url = serializers.HyperlinkedIdentityField(
            view_name = 'ingredient',
            lookup_field = 'id'
        )
        fields = ('id', 'url', 'name')
        # depth = 1
class Ingredients(ViewSet):

    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def create(self, request):
        new_ingredient = Ingredient()
        new_ingredient.name = request.data['name']
        new_ingredient.save()

    
        serializer = IngredientSerializer(new_ingredient, context = {'request': request})

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            ingredient = Ingredient.objects.get(pk=pk)
            serializer = IngredientSerializer(ingredient, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        ingredient = Ingredient.object.get(pk=pk)
        ingredient.name = request.data['name']
        ingredient.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            ingredient = Ingredient.objects.get(pk=pk)
            ingredient.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Ingredient.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        ingredients = Ingredient.objects.all()

        serializer = IngredientSerializer(
            ingredients, many=True, context={'request': request}
        )
        return Response(serializer.data)