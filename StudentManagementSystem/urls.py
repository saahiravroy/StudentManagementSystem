"""StudentManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from studentmanage.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('admin_login', admin_login, name='admin_login'),
    path('admin_home', admin_home, name='admin_home'),
    path('student_login', student_login, name='student_login'),
    path('add_Class', add_Class, name='add_Class'),
    path('manage_Class', manage_Class, name='manage_Class'),
    path('editClass/<int:pid>', editClass, name='editClass'),
    path('deleteClass/<int:pid>', deleteClass, name='deleteClass'),
    path('add_Student', add_Student, name='add_Student'),
    path('manage_Student', manage_Student, name='manage_Student'),
    path('editStudent/<int:pid>', editStudent, name='editStudent'),
    path('deleteStudent/<int:pid>', deleteStudent, name='deleteStudent'),
    path('add_Notice', add_Notice, name='add_Notice'),
    path('manage_Notice', manage_Notice, name='manage_Notice'),
    path('editNotice/<int:pid>', editNotice, name='editNotice'),
    path('deleteNotice/<int:pid>', deleteNotice, name='deleteNotice'),
    path('add_PublicNotice', add_PublicNotice, name='add_PublicNotice'),
    path('manage_PublicNotice', manage_PublicNotice, name='manage_PublicNotice'),
    path('editPubNotice/<int:pid>', editPubNotice, name='editPubNotice'),
    path('deletePubNotice/<int:pid>', deletePubNotice, name='deletePubNotice'),
    path('reportdate', reportdate, name='reportdate'),
    path('viewStudentDetails/<int:pid>', viewStudentDetails, name='viewStudentDetails'),
    path('search', search, name='search'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout/', Logout, name='logout'),
    path('user_home', user_home, name='user_home'),
    path('viewProfile', viewProfile, name='viewProfile'),
    path('viewNotice', viewNotice, name='viewNotice'),
    path('studentchangePassword', studentchangePassword, name='studentchangePassword'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
