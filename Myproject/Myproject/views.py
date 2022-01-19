from django.shortcuts import render

from Myproject.models import empmodel

from Myproject.serialize import empserializers

from rest_framework.response import Response

from rest_framework.decorators import api_view

@api_view(['GET'])
def showemp(request):

    results = empmodel.objects.all()

    searalize = empserializers(results, many=True)

    return Response(searalize.data)