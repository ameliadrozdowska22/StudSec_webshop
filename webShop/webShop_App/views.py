
from django.shortcuts import render
from django.http import HttpResponse

def webshop(request):

    context = {
        "main_image": "/media/main_image.jpg",
        "stickers": "/media/stickers_photo.png",
        "Hoodie": "/media/hoodie_photo.jpg",
        "t_shirt": "/media/t-shirt_photo.jpg"
    }

    return render(request, "webshop.html", context) 


def itemPage(request):

    context = {
        "main_image": "/media/main_image.jpg",
        "item_image": "/media/hoodie_photo.jpg",
    }

    return render(request, "itemPage.html", context) 