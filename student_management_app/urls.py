from django.urls import path, include
from . import views
from . import views_admin
from django.conf.urls.static import static
from School import settings

urlpatterns = [
    path('', views.showPage, name='homepage'),
    path('admin/', views_admin.showPageAdmin, name='admin_page'),
    path('login_page/', views.showLoginPage, name='login_page'),
    path('do/login/', views.doLogin, name='do_login'),
    path('do/logout/', views.doLogout, name='do_logout'),
    path('detail/user/', views.userDetail, name='detail'),
    path('do/add_staff/', views_admin.AddStaffView.as_view(), name='add_staff'),
    path('do/check/username/', views_admin.checkUsername, name='check_username'),
    path('do/check/course/', views_admin.checkCourseName, name='check_course_name'),
    path('do/add_course', views_admin.AddCourseView.as_view(), name='add_course'),
    path('do/add_student', views_admin.AddStudentView.as_view(), name='add_student'),
    path('do/add_subject', views_admin.AddSubjectView.as_view(), name='add_subject'),
    path('sub/mul', views_admin.add_subject, name='add_mul'),
    path('do/sub/mul', views_admin.do_add_sub, name='do_add_mul')

]