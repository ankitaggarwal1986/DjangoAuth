from urllib import response
from django.shortcuts import render
from . models import Employee, Tracking
from . serializers import EmployeeSerializer, TrackingSerializer, UserSerializer 
from rest_framework import generics
from rest_framework.serializers import Serializer
from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.
class RegisterdUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors, 'message': 'something went wrong'}) 

        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)

        return Response({'status': 200, 'payload':serializer.data, 'token': str(token_obj) ,'message': 'your data is saved'})

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Employee
    serializer_class = EmployeeSerializer

class TrackingList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer

class TrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Tracking
    serializer_class = TrackingSerializer
