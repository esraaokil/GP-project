from django.shortcuts import render
from .models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import  ProfileSerializer
from rest_framework import status, filters
# Create your views here.

#profile 
@api_view(['GET','POST'])
def profile_create(request):
    # GET
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = ProfileSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)