from rest_framework.viewsets import ModelViewSet

from .serializers import GenomeIndicatorSerializer, BacteriaSerializer, FileUploadSerializer
from .models import GenomeIndicator, Bacteria, FileUpload

class GenomeIndicatorViewSet(ModelViewSet):
    queryset = GenomeIndicator.objects.all()
    serializer_class = GenomeIndicatorSerializer

class BacteriaViewSet(ModelViewSet):
    queryset = Bacteria.objects.all()
    serializer_class = BacteriaSerializer

class FileUploadViewSet(ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
