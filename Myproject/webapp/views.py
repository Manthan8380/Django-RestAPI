from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees, User
from . serializers import employeesSerializer
import random


# Create your views here.

class employeesList(APIView):
    def get(self, request):
        products = employees.objects.all()
        serializer = employeesSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = employeesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        product = employees.objects.get(id=pk)
        serializer = employeesSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        product = employees.objects.get(id=pk)
        product.delete()
        # publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
