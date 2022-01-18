from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import ProductSerializer
from . models import Product


# Create your views here.
'''
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>',
    }
    return Response(api_urls)
'''
@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewDetail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Create(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    

@api_view(['POST'])
def Update(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)        

@api_view(['GET'])
def Delete(request, pk):
    products = Product.objects.get(id=pk)
    products.delete()

    return Response("Item delete success")
    