from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from notchlistApi.models import Beer_Serving_Style
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class BeerServingStyleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Beer_Serving_Style
        url = serializers.HyperlinkedIdentityField(
            view_name = 'beer_serving_style',
            lookup_field = 'id'
        )
        fields = ('id', 'url', 'name')
        # depth = 1
class Beer_Serving_Styles(ViewSet):

    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def create(self, request):
        new_beer_serving_style = Beer_Serving_Style()
        new_beer_serving_style.name = request.data['name']
        new_beer_serving_style.save()

    
        serializer = BeerServingStyleSerializer(new_beer_serving_style, context = {'request': request})

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            beer_serving_style = Beer_Serving_Style.objects.get(pk=pk)
            serializer = BeerServingStyleSerializer(beer_serving_style, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        beer_serving_style = Beer_Serving_Style.object.get(pk=pk)
        beer_serving_style.name = request.data['name']
        beer_serving_style.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            beer_serving_style = Beer_Serving_Style.objects.get(pk=pk)
            beer_serving_style.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Beer_Serving_Style.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        beer_serving_styles = Beer_Serving_Style.objects.all()

        serializer = BeerServingStyleSerializer(
            beer_serving_styles, many=True, context={'request': request}
        )
        return Response(serializer.data)