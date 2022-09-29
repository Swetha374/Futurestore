from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from owner.models import *

class CategoriesSerializer(ModelSerializer):
    class Meta:
        model=Categories
        fields="__all__"

class ProductsSerializer(ModelSerializer):

    class Meta:
        model=Products
        fields="__all__"


