from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def get_post_json(request):
    #curl -X POST http://localhost:8000/api/upload-data/
    #curl -X GET http://localhost:8000/api/upload-data/
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':
        return Response(status=status.HTTP_201_CREATED)