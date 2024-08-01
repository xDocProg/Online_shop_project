from .serializers import ReviewSerializer
from .models import Review
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
