from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponseRedirect
from rest_framework.parsers import JSONParser

from .models import *
import time,datetime
from .serializers import *
# Create your views here.




def Start(request):
    return render(request,'signin.html')

def SignIn(request):
    if request.method == 'POST':
       Username=request.POST['username']
       Name=request.POST['StudentID']
       Email=request.POST['email']
       Password=request.POST['password']
       admin= Admin()
       admin.Name=Name
       admin.Username=Username
       admin.Email=Email
       admin.Password=Password
       admin.save()
       time.sleep(2)
       return redirect(Home)
    else:
       return render(request,'signin.html')


def Home(request):
    today=datetime.date.today()
    return render(request,'homepage.html',{'today':today})

def AllStudents(request):
    allStudents=Student.objects.all()
    return render(request,'students.html',{'students':allStudents})

def deleteStd(request,uname):
    std=Student.objects.get(RollNo=uname)
    std.delete()
    return redirect(AllStudents)

def addStudent(request):
    if request.method == 'POST':
        rollno = request.POST['rollno']
        Name = request.POST['name']
        Email = request.POST['email']
        Password = request.POST['password']
        std=Student()
        std.RollNo=rollno
        std.StdName=Name
        std.Email=Email
        std.Password=Password
        std.save()
        return redirect(AllStudents)
    else:
        return redirect(AllStudents)




def getAttendance(request,date):
    today= datetime.date.today()
    if not Attendance.objects.filter(date=today).exists():
        std = Student.objects.all()
        for i in std:
            a = Attendance()
            a.student = i
            a.date = date
            a.save()

    if request.method == 'GET':
        attenadance = Attendance.objects.filter(date=date)
        serializer = AttendanceSerializer(attenadance, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        attenadance = Attendance.objects.filter(date=date)
        serializer = AttendanceSerializer(attenadance, many=True)
        return JsonResponse(serializer.data, safe=False)


def updateAttendance(request):
    checked=request.POST.getlist('att')
    today = datetime.date.today()
    Attendance.objects.all().update(status=False)
    for i in checked:
        std=Student.objects.get(RollNo=i)
        a=Attendance.objects.get(student=std,date=today)
        a.status=True
        a.save()
    return redirect(AttendancePage)

def AttendancePage(request):
    return render(request,'attendance.html')


