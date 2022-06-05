from rest_framework import serializers
from rest_framework.serializers import  ModelSerializer

from app.models import Categorie,Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product

        fields=['id',"nom","prix","categorie","date_created",'date_updated']

class CategorieDetailSerializer(ModelSerializer):
    products=serializers.SerializerMethodField()
    class Meta:
        model=Categorie
        fields=['id',"name","products"]



    def get_products(self,instance):
        queryset=instance.products.filter(active=True)
        serializer=ProductSerializer(queryset,many=True)
        return serializer.data

class CategorieListSerializer(ModelSerializer):

    class Meta:
        model = Categorie
        fields = ['id', "name"]

    def validate_name(self,value):
        if Categorie.objects.filter(name=value).exists():
            raise serializers.ValidationError("Catégorie existe déja")
        return value




