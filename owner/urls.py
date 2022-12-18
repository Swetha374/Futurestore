from django.urls import path
from owner import views

urlpatterns=[
    path("index",views.AdminDashboardView.as_view(),name="index"),
    path("orders/latest",views.OrdersListView.as_view(),name="neworders"),
    path("categories/list",views.ListCategoryView.as_view(),name="list-categories"),
    path("categories",views.AddCategoryView.as_view(),name="add-categories"),
    path("categories/edit/<int:id>",views.EditCategoryView.as_view(),name="edit-category"),
    path("orders/details/<int:id>",views.OrderDetailView.as_view(),name="order-details"),
    path("category/delete/<int:id>",views.delete_category,name="delete-category"),
    path("product/delete/<int:id>",views.delete_product,name="delete-product"),
    path("products/add",views.AddProductView.as_view(),name="add-product"),
    path("products/list", views.ListProductView.as_view(), name="list-products"),
    path("product/edit/<int:id>", views.EditProductView.as_view(), name="edit-product"),

]