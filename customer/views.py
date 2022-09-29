from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import CreateView,TemplateView,FormView,DetailView,DeleteView,ListView
from customer import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from owner.models import Products,Carts

class RegistrationView(CreateView):
    model=User
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("login")
    #<form action="" class="mt-5" method="post" enctype="multipart/form-data">  :
    # enctype="multipart/form-data" (reg cheyana tymil pro pic or pdf something non text data add cheyanel ith kodukanam formil html pagil

class LoginView(FormView):  #formview:used to render form withount using get
    template_name = "login.html"
    form_class = forms.LoginForm

    def post(self, request, *args, **kwargs):
        form=forms.LoginForm(request.POST,files=request.FILES)
        #POST:charactervalue,files=request.FILES: Image ,django returns request.data so no need to give like this
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})
        return render(request, "login.html")

class HomeView(TemplateView):
    template_name:str = "home.html"

    # def get_context_data(self, **kwargs:Any) ->Dict[str,Any]:   #e method ndha return cheyunne (dict(context)) :typescript(ini cheyendivarum
    def get_context_data(self, **kwargs): #extra context add cheyan
        context=super().get_context_data(**kwargs)
        all_products=Products.objects.all()
        context["products"]=all_products
        return context

class ProductDetailView(DetailView):
    template_name = "product-detail.html"
    model=Products
    context_object_name = "product"
    pk_url_kwarg = "id"

class AddToCartView(FormView):
    template_name = "add-to-cart.html"
    form_class =forms.CartForm

    #url id extract using get
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)

        return render(request,self.template_name,{"form":forms.CartForm(),"product":product})
                                                 #oru dic or contextil ethra key value pairdne venelum add cheyam

    #add to cart->Add (product add to cart by clicking Add)
    def post(self,request,*args,**kwargs):
        id = kwargs.get("id")
        product = Products.objects.get(id=id)
        qty=request.POST.get("qty") #get("name")->inspect cheythal kitum
        user=request.user
        Carts.objects.create(product=product,user=user,qty=qty) #add to cart
        messages.success(request,"item added to cart succesfully")
        return redirect("home")

class MyCartView(ListView):
    model = Carts
    template_name = "cart-list.html"
    context_object_name = "carts"


    #to override carts.objects.all(default orm)
    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)
    # remove items from cart (update as cancelled)
    #or
    #return Carts.objects.filter(user=self.request.user).exclude(status="cancelled") will rnot show cancelled products




