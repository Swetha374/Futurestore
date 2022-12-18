from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.serializers import *
from owner.models import Categories,Products,Carts
from rest_framework import authentication,permissions


class CategoriesView(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class =CategoriesSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]




class ProductsView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]









#category add
#product add,edit,delete