from rest_framework import serializers
from courses.models import Product, Lesson

class ProductSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(product=obj).count()

    class Meta:
        model = Product
        fields = ['id', 'name', 'start_date', 'price', 'lesson_count']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_link']
