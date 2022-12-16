from django.http import JsonResponse
from rest_framework import viewsets
from school.models import Student, Course
from serializer import StudentSerializer, CourseSerializer

class StudentsViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

# def students(request):
#   if request.method == 'GET':
#     student = {'id': 1, 'name': 'zephyr664'}
#     return JsonResponse(student)