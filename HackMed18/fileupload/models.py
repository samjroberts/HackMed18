from django.db import models

class FileUpload(models.Model):
    encodedFile = models.FileField('Uploaded file')
