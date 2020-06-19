from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from notchlistApi.models import Glassware
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class GlasswareSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Glassware
        url = serializers.HyperlinkedIdentityField(
            view_name = 'glassware',
            lookup_field = 'id'
        )
        fields = ('id', 'url', 'name', 'description','image_path')
        # depth = 1
class Glasswares(ViewSet):

    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def create(self, request):
        new_glassware = Glassware()
        new_glassware.name = request.data['name']
        new_glassware.description = request.data['description']
        new_glassware.image_path = request.data['image_path']
        new_glassware.save()

    
        serializer = GlasswareSerializer(new_glassware, context = {'request': request})

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            glassware = Glassware.objects.get(pk=pk)
            serializer = GlasswareSerializer(glassware, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        glassware = Glassware.object.get(pk=pk)
        glassware.name = request.data['name']
        glassware.description = request.data['description']
        glassware.image_path = request.data['image_path']
        glassware.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            glassware = Glassware.objects.get(pk=pk)
            glassware.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Glassware.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        glasswares = Glassware.objects.all()

        serializer = GlasswareSerializer(
            glasswares, many=True, context={'request': request}
        )
        return Response(serializer.data)