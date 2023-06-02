from django.urls import path
from .views import AdminLoginView, get_external_data

# , TeacherLoginView, StudentLoginView

urlpatterns = [
    path('admin/login/', AdminLoginView.as_view(), name='admin_login'),
    path('get-external-data/', get_external_data, name='get-external-data'),

    # path('teacher/login/', TeacherLoginView.as_view(), name='teacher_login'),
    # path('student/login/', StudentLoginView.as_view(), name='student_login'),
]
