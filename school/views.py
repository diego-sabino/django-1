from django.http import JsonResponse
from rest_framework import viewsets
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer

class StudentsViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = RegistrationSerializer
