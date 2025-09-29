
````markdown
# Image Caption Generator

A web application that automatically generates captions for uploaded images using AI. This project demonstrates image captioning using the **Hugging Face BLIP model**, **Celery** for asynchronous processing, and **Redis** as a caching and task broker system. The app is containerized with Docker for easy deployment.

---

## Features

- Upload any image and get an AI-generated caption.
- Captions are generated asynchronously using **Celery**, so large images don’t block the web app.
- **Redis** caching: repeated images return cached captions instantly.
- Supports multiple image formats: JPG, PNG.
- Gallery view to see all uploaded images and their captions.
- Modern, clean UI built with **Tailwind CSS**.

---

## Tech Stack

- **Python 3.10**
- **Django 5**
- **Celery** (asynchronous task queue)
- **Redis** (task broker & caching)
- **Hugging Face Transformers** (BLIP model for image captioning)
- **Pillow** (image processing)
- **Tailwind CSS** (UI styling)
- **Docker** (containerization)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/image-caption-generator.git
cd image-caption-generator
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Django

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

### 4. Run Redis

```bash
redis-server
```

or using Docker:

```bash
docker run -d --name redis-server -p 6379:6379 redis
```

### 5. Run Celery worker

```bash
celery -A imageproject worker -l info
```

### 6. Run Django server

```bash
python manage.py runserver
```

Open your browser at `http://127.0.0.1:8000` to use the app.

---

## Docker Installation (Recommended)

This project is also available as a pre-built Docker image on Docker Hub. Docker automatically pulls the image and runs it.

### Run the app via Docker:

```bash
# Start Redis
docker run -d --name redis-server -p 6379:6379 redis

# Run the Django app (pulls from Docker Hub automatically)
docker run -d -p 8000:8000 --name image-caption-generator --link redis-server \
    vineetnwt/image-caption-generator:latest
```

> Optional: To persist uploaded images:

```bash
docker run -d -p 8000:8000 -v $(pwd)/media:/app/media --link redis-server \
    vineetnwt/image-caption-generator:latest
```

---

## Usage

1. Visit `http://127.0.0.1:8000`.
2. Upload an image using the upload form.
3. Wait for the AI-generated caption (asynchronous, handled by Celery).
4. View uploaded images and captions in the gallery.

---

## How it works

1. **Image upload** → user uploads an image through the web form.
2. **Asynchronous processing** → Celery queues the caption generation task.
3. **Caption generation** → Hugging Face BLIP model generates a descriptive caption.
4. **Redis caching** → Repeated images are identified via hash and cached for faster response.
5. **Gallery view** → All uploaded images and their captions are displayed.

---

## Future Improvements

* Generate a **story or paragraph** based on the image using LLMs (e.g., Gemini API).
* Support bulk image uploads.
* Improve caching using image similarity instead of filename.
* Add user authentication and personalized galleries.

---

## License

MIT License

---

## Docker Hub

You can pull the pre-built image from [Docker Hub](https://hub.docker.com/repository/docker/vineetnwt/image-caption-generator) and run it directly without local setup.

```bash
docker run -d -p 8000:8000 vineetnwt/image-caption-generator:latest
```

> Note: Ensure Redis is running for asynchronous task handling.

---

## Contact

Developed by **Vineet**.
For questions, reach out via GitHub Issues or contact me directly.

```
