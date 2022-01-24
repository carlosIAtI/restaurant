from django.db import models
import uuid

# Create your models here.
class Restaurant(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombre_restaurant = models.CharField(max_length=255)
    correo = models.CharField(max_length=50)
    reseña = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

