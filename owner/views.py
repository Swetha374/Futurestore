from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView,View,CreateView,UpdateView
from owner.models import *
from owner.forms import OrderUpdateForm,CategoryForm,EditCategoryForm,ProductForm,EditProductForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib import messages

class AdminDashboardView(TemplateView):
    template_name = "owner/index.html"

    #to get cont of new orders
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)#to add an extra context
        count1=Orders.objects.filter(status="order-placed").count()
        count2=Carts.objects.filter(status="cancelled").count()
        count3=Categories.objects.all().count()
        count4=Products.objects.all().count()

        context["count1"]=count1
        context["count2"]=count2
        context["count3"]=count3
        context["count4"] =count4
        return context

class OrdersListView(ListView):
    model = Orders
    context_object_name = "orders"
    template_name = "owner/admin-listorder.html"

    def get_queryset(self):
        return Orders.objects.filter(status="order-placed")

class AddCategoryView(CreateView):
    template_name = "owner/add-category.html"
    form_class = CategoryForm
    success_url = reverse_lazy("list-categories")



class ListCategoryView(ListView):
    model = Categories
    context_object_name = "category"
    template_name = "owner/listcategory.html"

def delete_category(request,*args,**kwargs):
    id=kwargs.get("id")
    Categories.objects.get(id=id).delete()
    return redirect("list-categories")


class OrderDetailView(DetailView):
    model = Orders
    template_name ="owner/order-details.html"
    #order-details customer and owner conflit varathirikan vendi templateinakath vere folder owner enn create cheythu
    pk_url_kwarg = "id"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        form=OrderUpdateForm()
        context["form"]=form
        return context
    def post(self,request,*args,**kwargs):
        order=self.get_object()
        """detailview,updateview,deleteview: self.get_object ->specific objectne kitum allathe 
        id eduthit aha id ulla objectine edukenda avashyula"""

        print(self.get_object())
        form=OrderUpdateForm(request.POST)
        if form.is_valid():
            order.status=form.cleaned_data.get("status")
            order.expected_delivery_date=form.cleaned_data.get("expected_delivery_date")
            dt=form.cleaned_data.get("expected_delivery_date")
            order.save()
            send_mail(
                "order delivery update futurestore",   #sub
                f"your order will be delivered on{dt}",  #msg
                "swethasasi374@gmail.com",     #from
                ["ushasasi08@gmail.com"]  #order cheythitulla userde email id (, itit etra venelum add cheyam

            )

            print(form.cleaned_data)
            return redirect("index")

class EditCategoryView(UpdateView):
    model=Categories
    form_class =EditCategoryForm
    template_name = "owner/edit-category.html"
    pk_url_kwarg = "id"
    success_url =reverse_lazy("list-categories")

    def form_valid(self, form):
        messages.success(self.request, "category details has been changed")
        return super().form_valid(form)

class AddProductView(CreateView):
    model=Products
    template_name = "owner/add-product.html"
    form_class = ProductForm
    success_url = reverse_lazy("list-products")

    # def form_valid(self, form):
    #     form.instance.user=self.request.user #e form aan return super().form_valid(form) ile form
    #     messages.success(self.request, "product has been added")
    #     return super().form_valid(form)



class ListProductView(ListView):
    model = Products
    context_object_name = "product"
    template_name = "owner/listproduct.html"

def delete_product(request,*args,**kwargs):
    id=kwargs.get("id")
    Products.objects.get(id=id).delete()
    return redirect("list-products")


class EditProductView(UpdateView):
    model=Products
    form_class =EditProductForm
    template_name = "owner/edit-product.html"
    pk_url_kwarg = "id"
    success_url =reverse_lazy("list-products")

    def form_valid(self, form):
        messages.success(self.request, "product details has been changed")
        return super().form_valid(form)







