from django.shortcuts import render, redirect
from .form import ImageCaptionForm
from .models import ImageCaption
from .utils import generate_caption  
from captions.task import generate_caption_task,sub
from celery.result import AsyncResult

def upload_image(request):
    if request.method == "POST":
        form = ImageCaptionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            generate_caption_task.delay(instance.id) 
            return redirect("gallery")
    else:
        form = ImageCaptionForm()
    return render(request, "upload.html", {"form": form})
def gallery(request):
    images = ImageCaption.objects.all().order_by("-created_at")
    return render(request, "gallery.html", {"images": images})


def add_page(request):
    result = sub.delay(10,20)
    return render(request, "add.html", {"result": result})


def check_result(request, task_id):
    result = AsyncResult(task_id)
    return render(request, "result.html", { "result": result })






