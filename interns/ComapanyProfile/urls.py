from .views import CompanyView
from rest_framework.routers import DefaultRouter,SimpleRouter

router = SimpleRouter(trailing_slash=False)

# router = DefaultRouter()
router.register(r'comp', CompanyView, basename='user')

urlpatterns = router.urls