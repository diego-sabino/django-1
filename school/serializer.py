from rest_framework import serializers
from school.models import Student, Course, Registration

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'rg', 'cpf', 'birth_date']

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Registration
    fields = '__all__'

class RegistrationStudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Registration
    fields = ['course', 'timeCourse']

class RegistrationStudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Registration
    fields = ['course', 'timeCourse']

#atividade 2 incompleta