from .views import PhotoViewSet
from rest_freamwork.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cifar',PhotoViewSet)
urlpatterns = router.urls
