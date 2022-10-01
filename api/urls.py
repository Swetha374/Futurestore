from api.views import *
from rest_framework.routers import DefaultRouter                               #model viewset route cheyan router venam
from django.conf import settings
from django.conf.urls.static import static
router=DefaultRouter()
router.register("categories",CategoriesView,basename="categories")
router.register("products",ProductsView,basename="products")

urlpatterns=[

]+router.urls+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #user run timel upload cheythitulla image display aavel this is mandatory
