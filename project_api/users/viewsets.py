from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly

class ProfieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = ProfileSerializer