from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.db.models import F, FloatField
from django.db.models.functions import Coalesce
from .models import Product
from .forms import ProductForm, ProductCreateForm

# Create your views here.



def index_view(request):
    # return HttpResponse("<H1> Coders Caravan </H1>")
    context = {
        "text": "Hello World",
        "product_list": [1, 2, 3, 4, 5],
        "products": Product.objects.all(),
        "myproduct": Product.objects.last()
    }

    return render(request, "index.html", context)



def create_view(request):
    context = {
        "text": "Hello World",
        "product_list": [1, 2, 3, 4, 5],
        "products": Product.objects.all(),
        "myproduct": Product.objects.last()
    }
    return render(request, "index.html", context)




def detail_view(request, product_id, coders_id):
    context = {
        "product_id": product_id,
        "coders_id": coders_id,
    }
    return render(request, "detail.html", context)




def product_list_view(request):
    products = Product.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        total_price=F("price") - F("discount")
    )
    context = {
        "products": products
    }
    return render(request, "products/list.html", context)



def product_detail_view(request, id):
    product =  Product.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        total_price=F("price") - F("discount")
    ).get(id=id)

    context = {
        "product": product
    }
    return render(request, "products/detail.html", context)



def product_create_view(request):
    form = ProductForm()


    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            new_product = form.save(commit=False)

            # price = form.cleaned_data.get("price")
            # discount_price = form.cleaned_data.get("discount_price")
            #
            # total_price = price - (discount_price or 0)
            #
            # new_product.total_price = total_price
            """
            if commit=True --> Model.objects.create(...)
            if commit=False --> Model(...)
            """

            # new_product.discount_price = 0
            new_product.save()

            return redirect("mainapp:list")

    context = {
        "form": form
    }
    return render(request, "products/create.html", context)




def product_update_view(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            new_product = form.save()

            # new_product.discount_price = 0
            # new_product.save()

            return redirect("mainapp:list")

    context = {
        "form": form
    }
    return render(request, "products/update.html", context)




# def product_delete_view(request, id):
#     product = get_object_or_404(Product, id=id)
#     product.delete()
#     return redirect("products:list")



def product_create_add_view(request):
    form = ProductCreateForm()

    if request.method == "POST":
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "products/create.html", context)