from rest_framework import routers
from .viewsets import ProfieViewSet


app_name = 'users'

router = routers.DefaultRouter()
router.register('users', ProfieViewSet)