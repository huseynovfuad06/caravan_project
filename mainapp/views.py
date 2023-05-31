from django.shortcuts import render, HttpResponse
from django.db.models import F, FloatField
from django.db.models.functions import Coalesce
from .models import Product

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