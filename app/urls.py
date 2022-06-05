from django.urls import path, include

from app.views import CategorieView,ProductView
from rest_framework import routers

from app.views import AdminCategorieView

router=routers.SimpleRouter()
router.register("categorie",CategorieView,basename='categorie')
router.register("product",ProductView,basename="produit")
router.register("admin/categorie",AdminCategorieView,basename='categorie-admin')
urlpatterns = [
   path('',include(router.urls)),


]