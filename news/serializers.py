from rest_framework import serializers
from .models import News, NewsReview

class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    title = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return News.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
    

class NewsReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    feedback = serializers.CharField()
    reviewer_username = serializers.CharField(read_only=True, source="reviewer.username")
    news_id = serializers.SerializerMethodField()

    def get_news_id(self, value):
        return value.news.id

    def create(self, validated_data):
        return NewsReview.objects.create(**validated_data)
    
