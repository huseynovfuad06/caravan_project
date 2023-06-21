from django.urls import path
from . import views


app_name = "mainapp"

urlpatterns = [
    path("index/", views.index_view),
    path("create/coders/suzanna/", views.create_view),
    path("detail/<str:product_id>/<int:coders_id>/", views.detail_view),

    path("products/list/", views.product_list_view, name="list"),
    path("products/create/", views.product_create_view, name="create"),
    path("products/image/create/", views.create_product_image, name="create-image"),
    path("products/add/", views.product_create_add_view, name="add"),
    path("products/detail/<id>/", views.product_detail_view, name="detail"),
    path("products/update/<id>/", views.product_update_view, name="update"),

    path("products/wish/", views.wish_product_view, name="wish"),
]


