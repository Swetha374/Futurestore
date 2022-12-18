from django import forms
from owner.models import Carts,Categories,Products

class OrderUpdateForm(forms.Form):
    options=(
        ("dispatched", "dispatched"),
        ("in-transit", "in-transit"),
    )
    status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-select"})) #choicefield=selectfield,form-select=used to selectbox

    expected_delivery_date=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control","type":"date"})) #date field varan "type":"date"-> datepicker varan

class CategoryForm(forms.ModelForm):
    class Meta:
        model =Categories
        fields = '__all__'

class EditCategoryForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields="__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model =Products
        fields="__all__"

class EditProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields="__all__"