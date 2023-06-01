from rest_framework import routers
from .views import PacienteViewSet


router = routers.DefaultRouter()

router.register('pacientes', PacienteViewSet, basename='pacientes')

urlpatterns = router.urls