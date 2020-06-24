from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from notchlistApi.models import Beer, Drink_Style, Beer_Serving_Style
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class BeerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Beer
        url = serializers.HyperlinkedIdentityField(
            view_name = 'beer',
            lookup_field = 'id'
        )
        fields = ('id', 'url', 'user_id', 'name', 'drink_style_id', 'location_name','location_address', 'brewery', 'rating', 'description', 'abv', 'ibu', 'beer_serving_style_id', 'image_path', 'created_at', 'user', 'drink_style', 'beer_serving_style')
        depth = 2
class Beers(ViewSet):

    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def create(self, request):
        new_beer = Beer()
        new_beer.user = request.auth.user
        new_beer.name = request.data['name']
        new_beer.drink_style_id = request.data['drink_style_id']
        new_beer.location_name = request.data['location_name']
        new_beer.location_address = request.data['location_address']
        new_beer.brewery = request.data['brewery']
        new_beer.rating = request.data['rating']
        new_beer.description = request.data['description']
        new_beer.abv = request.data['abv']
        new_beer.ibu = request.data['ibu']
        new_beer.beer_serving_style_id = request.data['beer_serving_style_id']
        new_beer.image_path = request.data['image_path']
        new_beer.created_at = request.data['created_at']
        new_beer.save()

    
        serializer = BeerSerializer(new_beer, context = {'request': request})

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            beer = Beer.objects.get(pk=pk)
            serializer = BeerSerializer(beer, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        beer = Beer.objects.get(pk=pk)
        beer.name = request.data['name']
        beer.drink_style_id = request.data['drink_style_id']
        beer.location_name = request.data['location_name']
        beer.location_address = request.data['location_address']
        beer.brewery = request.data['brewery']
        beer.rating = request.data['rating']
        beer.description = request.data['description']
        beer.abv = request.data['abv']
        beer.ibu = request.data['ibu']
        beer.beer_serving_style_id = request.data['beer_serving_style_id']
        beer.image_path = request.data['image_path']
        beer.created_at = request.data['created_at']
        beer.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            beer = Beer.objects.get(pk=pk)
            beer.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Beer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        
        beers = Beer.objects.filter(user=self.request.user)

        serializer = BeerSerializer(
            beers, many=True, context={'request': request}
        )
        return Response(serializer.data)