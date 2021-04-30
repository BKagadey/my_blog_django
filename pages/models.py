from django.db import models

# Create your models here.

class Pages(models.Model):
    page_image = models.ImageField(upload_to='page_images/')
    page_text = models.CharField(max_length=300)