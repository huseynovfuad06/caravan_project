from django.urls import path
from . import views


app_name = "mainapp"

urlpatterns = [
    path("index/", views.index_view),
    path("create/coders/suzanna/", views.create_view),
    path("detail/<str:product_id>/<int:coders_id>/", views.detail_view),

    path("products/list/", views.product_list_view, name="list"),
    path("products/detail/<id>/", views.product_detail_view, name="detail"),
]


