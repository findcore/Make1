from django.db import models

class FileUpload(models.Model):
    title = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to="img/", blank=True)

    def __str__(self):
        return self.title