from django import forms
from .models import ImageCaption

class ImageCaptionForm(forms.ModelForm):
    class Meta:
        model = ImageCaption
        fields = ["image"]
