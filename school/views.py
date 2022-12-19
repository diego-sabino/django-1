from django.http import JsonResponse
from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, RegistrationStudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
  queryset = Registration.objects.all()
  serializer_class = RegistrationSerializer

class RegistrationStudentViewSet(generics.ListAPIView):
  def get_queryset(self):
    queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
    return queryset
  serializer_class = RegistrationStudentSerializer