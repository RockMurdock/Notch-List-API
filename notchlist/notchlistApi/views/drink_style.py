from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from notchlistApi.models import Drink_Style
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class DrinkStyleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Drink_Style
        url = serializers.HyperlinkedIdentityField(
            view_name = 'drink_style',
            lookup_field = 'id'
        )
        fields = ('id', 'url', 'name', 'description','glassware_id')
        # depth = 1
class Drink_Styles(ViewSet):

    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def create(self, request):
        new_drink_style = Drink_Style()
        new_drink_style.name = request.data['name']
        new_drink_style.description = request.data['description']
        new_drink_style.glassware_id = request.data['glassware_id']
        new_drink_style.save()

    
        serializer = DrinkStyleSerializer(new_glassware, context = {'request': request})

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            drink_style = Drink_Style.objects.get(pk=pk)
            serializer = DrinkStyleSerializer(drink_style, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        drink_style = Drink_Style.object.get(pk=pk)
        drink_style.name = request.data['name']
        drink_style.description = request.data['description']
        drink_style.glassware_id = request.data['glassware_id']
        drink_style.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            drink_style = Drink_Style.objects.get(pk=pk)
            drink_style.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Drink_Style.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        drink_styles = Drink_Style.objects.all()

        serializer = DrinkStyleSerializer(
            drink_styles, many=True, context={'request': request}
        )
        return Response(serializer.data)