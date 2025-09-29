from django.db import models

class ImageCaption(models.Model):
    image = models.ImageField(upload_to="uploads/")   # store uploaded image
    caption = models.TextField(blank=True, null=True) # AI-generated caption
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption if self.caption else "No Caption Yet"

