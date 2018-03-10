from rest_framework.viewsets import ModelViewSet

from .serializers import GenomeIndicatorSerializer, BacteriaSerializer
from .models import GenomeIndicator, Bacteria

class GenomeIndicatorViewSet(ModelViewSet):
    queryset = GenomeIndicator.objects.all()
    serializer_class = GenomeIndicatorSerializer

class BacteriaViewSet(ModelViewSet):
    queryset = Bacteria.objects.all()
    serializer_class = BacteriaSerializer
