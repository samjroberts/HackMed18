from .api import GenomeIndicatorViewSet, BacteriaViewSet, FileUploadViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('genomeindicators', GenomeIndicatorViewSet)
router.register('bacteria', BacteriaViewSet)
router.register('files', FileUploadViewSet)

urlpatterns = router.urls
