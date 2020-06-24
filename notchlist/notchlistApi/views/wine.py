from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from notchlistApi.models import Wine, Drink_Style
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class WineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Wine
        url = serializers.HyperlinkedIdentityField(
            view_name = 'wine',
            lookup_field = 'id'
        )
        fields = ('id', 'url', 'user_id', 'name', 'drink_style_id', 'location_name','location_address', 'winery', 'rating', 'description', 'abv', 'year', 'image_path', 'created_at', 'user', 'drink_style')
        depth = 2
class Wines(ViewSet):

    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def create(self, request):
        new_wine = Wine()
        new_wine.user = request.auth.user
        new_wine.name = request.data['name']
        new_wine.drink_style_id = request.data['drink_style_id']
        new_wine.location_name = request.data['location_name']
        new_wine.location_address = request.data['location_address']
        new_wine.winery = request.data['winery']
        new_wine.rating = request.data['rating']
        new_wine.description = request.data['description']
        new_wine.abv = request.data['abv']
        new_wine.year = request.data['year']
        new_wine.image_path = request.data['image_path']
        new_wine.created_at = request.data['created_at']
        new_wine.save()

    
        serializer = WineSerializer(new_wine, context = {'request': request})

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            wine = Wine.objects.get(pk=pk)
            serializer = WineSerializer(wine, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        wine = Wine.objects.get(pk=pk)
        wine.name = request.data['name']
        wine.drink_style_id = request.data['drink_style_id']
        wine.location_name = request.data['location_name']
        wine.location_address = request.data['location_address']
        wine.winery = request.data['winery']
        wine.rating = request.data['rating']
        wine.description = request.data['description']
        wine.abv = request.data['abv']
        wine.year = request.data['year']
        wine.image_path = request.data['image_path']
        wine.created_at = request.data['created_at']
        wine.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            wine = Wine.objects.get(pk=pk)
            wine.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Wine.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        wines = Wine.objects.filter(user=self.request.user)

        serializer = WineSerializer(
            wines, many=True, context={'request': request}
        )
        return Response(serializer.data)