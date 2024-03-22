# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField

class MyModel(models.Model):
    image = CloudinaryField('image')