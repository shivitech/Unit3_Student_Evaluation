from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("students/", views.student_list, name="student_list"),
    path("student/<int:student_id>/", views.student_detail, name="student_detail"),
    path("add-student/", views.add_student, name="add_student"),
]