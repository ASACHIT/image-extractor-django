from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
import wget

from .imgextractor import Assets


def index(request: HttpRequest):

    if request.method == "POST":
        url = request.POST.get("link")
        if url.startswith("https"):
            print(url)
            get_images = Assets(url)
            links_ = get_images.pull_images()

            return render(request, "index.html", context={"imageslink": links_})
        else:
            return redirect("homepage")

    return render(request, "index.html")
