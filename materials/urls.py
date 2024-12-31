from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CourseViewSet, LessonListCreate, LessonDetail

app_name = 'materials'

router = SimpleRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonListCreate.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonDetail.as_view(), name='lesson-detail'),
]
