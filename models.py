from django.db import models
import os



# Create your models here.
class Plants(models.Model):
    image = models.ImageField(upload_to='static/assets/images')

    def filename(self):
        return os.path.basename(self.image.name)


