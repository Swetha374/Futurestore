from api.views import *
from rest_framework.routers import DefaultRouter                               #model viewset route cheyan router venam
router=DefaultRouter()
router.register("categories",CategoriesView,basename="categories")
router.register("products",ProductsView,basename="products")

urlpatterns=[

]+router.urls