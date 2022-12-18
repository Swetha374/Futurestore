from django.urls import path
from customer import views


urlpatterns=[
   path("",views.LoginView.as_view(),name="login"),
   path("signout",views.SignOutView.as_view(),name="logout"),
   path("register",views.RegistrationView.as_view(),name="register"),
   path("home",views.HomeView.as_view(),name="home"),
   path("products/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
   path("products/<int:id>/carts/add",views.AddToCartView.as_view(),name="add-to-cart"),
   path("carts/all",views.MyCartView.as_view(),name="mycart"),
   path("cart/remove/<int:id>", views.cartitem_remove, name="removeitem"),
   path("carts/placeorder/<int:cid>/<int:pid>",views.PlaceOrderView.as_view(),name="place-order"),  #cid=cartid,pid



]