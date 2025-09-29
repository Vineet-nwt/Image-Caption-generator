import hashlib
from .redis_client import redis_client
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    with open(image_path, "rb") as f:
        file_bytes = f.read()
        image_hash = hashlib.md5(file_bytes).hexdigest() 
    
    cache_key = f"caption:{image_hash}"

    cached_caption = redis_client.get(cache_key)
    if cached_caption:
        print("⚡ Using cached caption")
        return cached_caption

    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs, max_length=50, num_beams=5, no_repeat_ngram_size=2)
    caption = processor.decode(out[0], skip_special_tokens=True)

    redis_client.setex(cache_key, 86400, caption)

    return caption
