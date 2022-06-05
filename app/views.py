from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Categorie,Product
from rest_framework.viewsets import ReadOnlyModelViewSet
from app.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet

from app.serializers import CategorieDetailSerializer,CategorieListSerializer


class CategorieView(ReadOnlyModelViewSet):
    serializer_class = CategorieListSerializer
    detail_serializer_class=CategorieDetailSerializer

    def get_queryset(self):
        return Categorie.objects.all()

    def get_serializer_class(self):
        if self.action=="retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
class ProductView(ReadOnlyModelViewSet):
   serializer_class = ProductSerializer
   def get_queryset(self):
       queryset=Product.objects.filter(active=True)
       category_id=self.request.GET.get("category_id")
       if category_id is not None:
           queryset=queryset.filter(categorie_id=category_id)
           return queryset

class AdminCategorieView(ModelViewSet):
    serializer_class = CategorieListSerializer
    detail_serializer_class=CategorieDetailSerializer

    def get_queryset(self):
        return Categorie.objects.all()