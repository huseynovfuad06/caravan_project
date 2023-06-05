from django import forms
from .models import Product



# class ProductForm(forms.Form):
#     name = forms.CharField()
#     description = forms.CharField()
#     price = forms.FloatField()



class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = ("name", "description", "price", "discount_price")
        # exclude = ("created_at", "updated_at", "discount_price")
        fields = "__all__"