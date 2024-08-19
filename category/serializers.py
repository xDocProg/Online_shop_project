from typing import List, Dict, Any

from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'subcategories']

    def get_subcategories(self, obj: Category) -> List[Dict[str, Any]]:
        return CategorySerializer(obj.subcategories.all(), many=True).data
