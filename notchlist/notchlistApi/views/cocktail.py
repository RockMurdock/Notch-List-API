from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from notchlistApi.models import Cocktail
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class CocktailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cocktail
        url = serializers.HyperlinkedIdentityField(
            view_name = 'cocktail',
            lookup_field = 'id'
        )
        fields = ('id', 'url', 'user_id', 'name', 'location_name','location_address', 'rating', 'description', 'image_path')
        # depth = 1
class Cocktails(ViewSet):

    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def create(self, request):
        new_cocktail = Cocktail()
        new_cocktail.user = request.auth.user
        new_cocktail.name = request.data['name']
        new_cocktail.location_name = request.data['location_name']
        new_cocktail.location_address = request.data['location_address']
        new_cocktail.rating = request.data['rating']
        new_cocktail.description = request.data['description']
        new_cocktail.image_path = request.data['image_path']
        new_cocktail.save()

    
        serializer = CocktailSerializer(new_cocktail, context = {'request': request})

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            cocktail = Cocktail.objects.get(pk=pk)
            serializer = CocktailSerializer(cocktail, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        cocktail = Cocktail.object.get(pk=pk)
        cocktail.name = request.data['name']
        cocktail.location_name = request.data['location_name']
        cocktail.location_address = request.data['location_address']
        cocktail.rating = request.data['rating']
        cocktail.description = request.data['description']
        cocktail.image_path = request.data['image_path']
        cocktail.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            cocktail = Cocktail.objects.get(pk=pk)
            cocktail.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Cocktail.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        cocktails = Cocktail.objects.all()

        serializer = CocktailSerializer(
            cocktails, many=True, context={'request': request}
        )
        return Response(serializer.data)