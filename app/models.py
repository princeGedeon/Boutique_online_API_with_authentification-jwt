from django.db import models

# Create your models here.
class Categorie(models.Model):
    name=models.CharField(max_length=255)

class Product(models.Model):
    nom=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    prix=models.IntegerField()
    categorie=models.ForeignKey(Categorie,related_name="products",on_delete=models.CASCADE)
    active=models.BooleanField(default=False)

