from rest_framework import serializers
from . models import MoviesData

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length = None, use_url = True)
    class Meta:
        model = MoviesData
        fields = ['id', 'name', 'description', 'duration', 'rating', 'genere', 'image']
