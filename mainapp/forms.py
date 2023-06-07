from django import forms
from .models import Product
from .validators import validate_timestamp



# class ProductForm(forms.Form):
#     name = forms.CharField()
#     description = forms.CharField()
#     price = forms.FloatField()



class ProductForm(forms.ModelForm):
    timestamp = forms.CharField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        # validators=[validate_timestamp]
    )

    class Meta:
        model = Product
        # fields = ("name", "description", "price", "discount_price")
        # exclude = ("created_at", "updated_at", "discount_price")
        fields = "__all__"


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        # print(self.fields)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        # self.fields['name'].widget.attrs.update({"class": "form-control underline"})
        self.fields['name'].widget.attrs["class"] += " underline"
    
    
    
    def clean(self):
        price = self.cleaned_data.get("price", None)
        discount_price = self.cleaned_data.get("discount_price", None)

        if not price:
            raise forms.ValidationError("Price is required")


        if price == discount_price:
            raise forms.ValidationError("Discount price must be lower than price")

        return super().clean()


    def save(self, commit=True):
        print(self.cleaned_data)

        if commit:
            return Product.objects.create(
                **self.cleaned_data
            )
        return Product(**self.cleaned_data)





class ProductCreateForm(forms.ModelForm):
    tax_price = forms.FloatField(label="TAX price")
    class Meta:
        model = Product
        fields = ("name", "description", "price", "discount_price")
        # widgets = {
        #     "name":
        # }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": f"{field} form-control"})
            self.fields[field].required = False


    def clean(self):
        price = self.cleaned_data.get("price")
        discount = self.cleaned_data.get("discount_price", 0)
        tax = self.cleaned_data.get("tax_price", 0)

        if (price - discount + tax) == 0:
            raise forms.ValidationError("Price tax_price ile discount_price-in ferqinden boyuk olmalidir")
        
        return super().clean()


    def save(self, commit=True):
        self.cleaned_data["name"] = self.cleaned_data["name"].upper()
        del self.cleaned_data["tax_price"]

        if commit:
            return Product.objects.create(
                **self.cleaned_data
            )

        return Product(**self.cleaned_data)

