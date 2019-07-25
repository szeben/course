from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializer

# Create your views here.
class ListCreateCourses(APIView):
    def get(self, request, format=None):
        courses = models.Courses.objects.all()
        serializers = serializer.CoursesSerializer(courses, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers =  serializer.CoursesSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)