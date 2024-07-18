from django.http import JsonResponse
from .models import Gym
from .serializers import GymSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET', 'POST'])
def gym_list(request,format=None):
    
    if request.method == 'GET':
        gyms=Gym.objects.all()
        serializer=GymSerializer(gyms,many=True)
        # import pdb;pdb.set_trace()
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        serializer=GymSerializer(data=request.data)
        # import pdb;pdb.set_trace()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)     


@api_view(['GET','PATCH','DELETE'])
def gym_detail(request,id,format=None):
    try:
        gym=Gym.objects.get(pk=id)
    except Gym.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=GymSerializer(gym)
        return Response(serializer.data)
    if request.method == 'PATCH':
         serializer=GymSerializer (gym, data=request.data,partial=True)
         if serializer.is_valid():
             
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'DELETE':
        gym.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
