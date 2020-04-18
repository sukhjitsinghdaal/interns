from .views import CategoryView,StateView
from rest_framework.routers import DefaultRouter,SimpleRouter

router = SimpleRouter(trailing_slash=False)

# router = DefaultRouter()
router.register(r'category', CategoryView, basename='user')
router.register(r'state', StateView, basename='user')

urlpatterns = router.urls