from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.db import models
from io import BytesIO

from .services import get_concise

def home_page_view(request):
    done = False

    if request.method == "POST":
        slideshow = request.FILES.get("slides")

        done = 1

        if slideshow:
            file = BytesIO(slideshow.read())
            concise_slideshow = get_concise(file) 

            concise_file = BytesIO()
            concise_slideshow.save(concise_file)
            concise_file.seek(0)

            return FileResponse(concise_file, as_attachment=True, filename = "concise_slides.pptx")
        else:
            return HttpResponse("Failed")

    return render(request, "home.html", {"done":done})

def download_slides(request, slideshow):
    return FileResponse(slideshow, as_attachment=True, filename = "concise_slides.pptx")
