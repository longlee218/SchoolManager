"""School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from School import settings
from student_management_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Long/', include('student_management_app.urls'))
    # path('demo/', views.showPage, name='home')
]+static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,
                                                                        document_root=settings.STATIC_ROOT)
