from django.contrib import admin

from .models import GenomeIndicator, Bacteria, FileUpload

admin.site.register(GenomeIndicator)
admin.site.register(Bacteria)
admin.site.register(FileUpload)
