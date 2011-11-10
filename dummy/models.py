from django.db import models

# Create your models here.
from imagekit.models import ProcessedImageField, ImageSpec
from imagekit.processors import resize


class Dummy(models.Model):
    name = models.TextField(blank=True)
    spec_image = ProcessedImageField(
            [resize.Fit(width=600, height=600)],
            upload_to = 'large_view',
            format = 'JPEG',
            # quality = 60,
            )
    thumbnail = ImageSpec(
            [resize.Crop(90, 90)],
            image_field='spec_image',
            format = 'JPEG',
            quality = 60,
            )

