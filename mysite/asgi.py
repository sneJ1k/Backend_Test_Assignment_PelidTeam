import os
import django
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

django_asgi_app = get_asgi_application()

from places.api import app as fastapi_app  # noqa: E402

app = FastAPI()
app.mount("/api", fastapi_app)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")
app.mount("/", django_asgi_app)
