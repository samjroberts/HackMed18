from .api import GenomeIndicatorViewSet, BacteriaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('genomeindicators', GenomeIndicatorViewSet)
router.register('bacteria', BacteriaViewSet)

urlpatterns = router.urls
