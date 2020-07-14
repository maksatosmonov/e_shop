from django import forms
from product.models import *


class ProductForm(forms.ModelForm):
    class Meta:
         model = Product
         fields = [
             "name",
             "category",
             "photo",
             "description",
             "price"
             ]    
