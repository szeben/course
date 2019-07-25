from django.shortcuts import get_object_or_404
from rest_framework import generics
from . import models
from . import serializer

# Create your views here.
class ListCreateCourses(generics.ListCreateAPIView):
    queryset = models.Courses.objects.all()
    serializer_class = serializer.CoursesSerializer

class RetrieveUpdateDestroyCourses(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Courses.objects.all()
    serializer_class = serializer.CoursesSerializer

class ListCreateReview(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializer.ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

    def perform_create(self, serializer):
        course = get_object_or_404(
            models.Courses, pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)
    

class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializer.ReviewSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            course_id=self.kwargs.get('course_pk'),
            pk=self.kwargs.get('pk')
        )
