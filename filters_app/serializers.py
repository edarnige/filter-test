from rest_framework import serializers

from . import models

class BlogSerializer(serializers.Serializer):
    ''' Serializer for INV metadata '''
    name = serializers.CharField(max_length=100)
    tagline = serializers.CharField(max_length=100)

    # class Meta:
    #     model = models.Blog
    #     fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    ''' Serializer for entry objects '''
    
    blog = BlogSerializer()

    class Meta:
        model = models.Entry
        fields = '__all__'
        depth = 2