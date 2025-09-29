# captions/tasks.py
from celery import shared_task
from .models import ImageCaption
from .utils import generate_caption
from time import sleep

@shared_task
def generate_caption_task(image_id):
    try:
        img = ImageCaption.objects.get(id=image_id)
        caption = generate_caption(img.image.path)
        img.caption = caption
        img.save()
        return caption
    except ImageCaption.DoesNotExist:
        return "Image not found"
    

@shared_task
def sub(x,y):
    sleep(10)
    return x-y
