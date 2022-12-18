from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import CreateView,TemplateView,FormView,DetailView,DeleteView,ListView,UpdateView,View
from customer import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from owner.models import Products,Carts,Orders,Categories

class RegistrationView(CreateView):
    model=User
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("login")
    #<form action="" class="mt-5" method="post" enctype="multipart/form-data">  :
    # enctype="multipart/form-data" (reg cheyana tymil pro pic or pdf something non text data add cheyanel ith kodukanam formil html pagil
    def form_valid(self,form):
        messages.success(self.request,"Your account has been created")
        return super().form_valid(form)

class LoginView(FormView):  #formview:used to render form withount using get
    template_name = "signin.html"
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
                if request.user.is_superuser:
                    return redirect("index")
                else:
                    return redirect("home")
            else:
                return render(request,"signin.html",{"form":form})
        return render(request, "signin.html")

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")




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
        id= kwargs.get("id")
        product = Products.objects.get(id=id)
        qty=request.POST.get("qty") #get("name")->inspect cheythal kitum
        user=request.user
        Carts.objects.create(product=product,user=user,qty=qty) #add to cart
        messages.success(request,"item added to cart succesfully")
        return redirect("home")

class MyCartView(ListView):
    model = Carts
    template_name = "cart-list.html"
    context_object_name = "carts"  #for cart in carts(context)


    #to override carts.objects.all(default orm)
    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-created_date")
        #order_by sort ascending, order_by("-created_date")->sort descending

    # remove items from cart (update as cancelled)
    #or
    #return Carts.objects.filter(user=self.request.user).exclude(status="cancelled") will rnot show cancelled products


class PlaceOrderView(FormView):
    template_name = "place-order.html"
    form_class = forms.OrderForm

    #checkout click=> carts/placeorder/cartid/productid
    def post(self, request, *args, **kwargs):  #...=spread operator
        cart_id=kwargs.get("cid")
        product_id=kwargs.get("pid")
        cart=Carts.objects.get(id=cart_id)
        product=Products.objects.get(id=product_id)
        user=request.user #logged user
        delivery_address=request.POST.get("delivery_address")
        Orders.objects.create(product=product,user=user,delivery_address=delivery_address)
        cart.status="order-placed" #order place cheythal status
        cart.save()
        return redirect("home")
def cartitem_remove(request, *args, **kwargs):
    cart_id = kwargs.get("id")
    print(cart_id)
    cart = Carts.objects.get(id=cart_id)
    cart.status = "cancelled"
    cart.save()
    messages.success(request, "Item removed...")
    return redirect("mycart")