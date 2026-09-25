from django.urls import path
from . import views


urlpatterns=[
    path('students/add/',views.register,name='register_url'),
    path("students/",views.table,name='table_url'),
    path('students/update/<int:sid>', views.update_statudent_view, name='update_statudent_view'),
    path("students/delete/<int:sid>/",views.delete,name='delete_student'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path("logout/",views.logout_view,name='logout'),
    path("login/",views.login_view,name='login'),
    # teacher
    path("teachers/",views.Teacher,name='teachers'),
    path("add_teachers/",views.add_teachers,name='add_teachers'),
    path("edit/<int:tid>",views.edit_teacher,name="edit_teacher"),
    path("delete/<int:tid>",views.delete_teacher,name='delete_teacher'),
    # Notification
    path("notification/",views.notification,name='notification'),
    # attendance
    path('attendance/',views.attendance,name='attendance'),


]