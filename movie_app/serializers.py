from rest_framework import serializers
from .models import Video, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'video', 'user', 'content', 'created_at']

class VideoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'uid', 'title', 'description', 'video_file', 'user', 'likes', 'likes_count', 'comments', 'created_at']

    def get_likes_count(self, obj):
        return obj.likes.count()
