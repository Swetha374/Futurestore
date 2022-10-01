from django.urls import path
from owner import views

urlpatterns=[
    path("index",views.AdminDashboardView.as_view(),name="dashboard"),
]