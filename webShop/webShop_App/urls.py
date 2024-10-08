from django.urls import path
from webShop_App import views

urlpatterns = [
    path('', views.webshop, name='webshop'),
    path('itemPage', views.itemPage, name="itemPage")
]