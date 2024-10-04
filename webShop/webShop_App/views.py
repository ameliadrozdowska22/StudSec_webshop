
from django.shortcuts import render
from django.http import HttpResponse

def webshop(request):

    context = {
        "main_image": "/media/main_image.jpg",
    }

    return render(request, "webshop.html", context) 