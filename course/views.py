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