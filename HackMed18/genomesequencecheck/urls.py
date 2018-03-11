from .api import GenomeIndicatorViewSet, BacteriaViewSet, FileUploadViewSet
from rest_framework.routers import DefaultRouter
from .views import get_sequencing_results
from django.urls import path, include

router = DefaultRouter()
router.register('genomeindicators', GenomeIndicatorViewSet)
router.register('bacteria', BacteriaViewSet)
router.register('files', FileUploadViewSet)

urlpatterns = [
    path('get_sequencing_results/', get_sequencing_results)
] + router.urls
