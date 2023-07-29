from rest_framework import serializers
from news.models import New

class NewsSerialzer(serializers.ModelSerializer):
    # date = serializers.ReadOnlyField()
    
    class Meta:
        model = New
        fields = ['id', 'title', 'text', 'author', 'date']

#serializer file