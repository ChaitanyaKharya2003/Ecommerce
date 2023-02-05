from django.urls import path
from . import views
from django.contrib import admin
admin.site.site_header = 'Own Website'
admin.site.site_title= "Website admin"
admin.site.index_title="Website admin"

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path('shop/', views.handleSignUp, name="handleSignUp"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handleLogout"),


]

