from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import generics
from rest_framework.serializers import Serializer 
from django.db.models.query import QuerySet
# Create your views here.

class BuyerList(generics.ListCreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class BuyerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buyer
    serializer_class = BuyerSerializer

class MachineList(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine
    serializer_class = MachineSerializer

class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale
    serializer_class = SaleSerializer


