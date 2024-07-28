from .serializers import ReviewSerializer
from .models import Review
from rest_framework import viewsets


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
