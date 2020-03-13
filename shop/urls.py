from django.urls import path
from . import views

urlpatterns = [
    path('',views.index4, name="index4"),
    path("about/", views.about, name="aboutUs"),
    path("contact/", views.contact, name="contactUs"),
    path("tracker/", views.tracker, name="trackingstatus"),
    path("search", views.search, name="searchproduct"),
    path("products/<int:myid>", views.productview, name="productview"),
    path("checkout/", views.checkout, name="checkout"),
]