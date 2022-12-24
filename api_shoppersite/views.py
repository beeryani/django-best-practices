from rest_framework.response import Response
from rest_framework.decrotators import api_view

@api_view(['GET'])
def getData(request):
    return Response({'name': 'Dennis', 'age': 28})
    