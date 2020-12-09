from django.urls import path, re_path
from course import views

urlpatterns = [
    re_path(r"category/(?P<pk>\d+)", views.CourseCategoryAPIView.as_view()),
    path("courses/", views.CourseAPIView.as_view()),
    re_path(r"^chapters/$", views.CourseChapterAPIView.as_view()),
]
