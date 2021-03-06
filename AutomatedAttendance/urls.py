"""AutomatedAttendance URL Configuration

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
from django.urls import path
from Attendance.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Start,name="Start"),
    path('SignIn',SignIn,name='SignIn'),
    path('Home',Home,name='Home'),
    path('Students',AllStudents,name='Students'),
    path('Students/Delete/<slug:uname>',deleteStd,name='delStd'),
    path('Students/Add',addStudent,name='addStd'),
    path('Attendance/<slug:date>',getAttendance,name='getAttendance'),
    path('AttendancePage', AttendancePage, name='AttendancePage'),
    path('UpdateAttendance',updateAttendance,name='updateAttendance'),
    path('LiveStream',liveStream,name='liveStream'),
    path('SignUp',mySignIn,name='mySignIn'),
    path('viewAttendance/<slug:rollNo>',viewAttendance,name='viewAttendance'),
    path('MarkAttendance',MarkAttendance,name='MarkAttendance'),
 
]
