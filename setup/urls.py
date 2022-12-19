from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CourseViewSet, RegistrationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename="Students")
router.register('courses', CourseViewSet, basename="Courses")
router.register('registration', RegistrationViewSet, basename="Registrations")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
