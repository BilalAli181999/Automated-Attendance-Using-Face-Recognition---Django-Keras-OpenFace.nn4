from django.http import HttpResponse, JsonResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
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
        std=Student()
        std.RollNo=rollno
        std.StdName=Name
        std.Email=Email
        std.save()
        return redirect(AllStudents)
    else:
        return redirect(AllStudents)




def getAttendance(request,date):
    if not Attendance.objects.filter(date=date).exists():
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
    checked=request.POST.getlist('att[]')
    today = request.POST['date']
    Attendance.objects.filter(date=today).update(status=False)
    for i in checked:
        std=Student.objects.get(RollNo=i)
        a=get_object_or_404(Attendance, student=std,date=today)
        a.status=True
        a.save()
    html="Success"    
    return HttpResponse(html)

def AttendancePage(request):
    today=datetime.date.today()
    if not Attendance.objects.filter(date=today).exists():
            std = Student.objects.all()
            for i in std:
                  a = Attendance()
                  a.student = i
                  a.date = today
                  a.save()
    return render(request,'attendance.html')

def liveStream(request):
    return render(request, 'liveStream.html')

def mySignIn(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        name = Admin.objects.get(Username=username)
    except Admin.DoesNotExist:
        name = None
    try:
        stdPassword = Admin.objects.get(Password=password ,Username=username)
    except Admin.DoesNotExist:
        stdPassword = None
    status=False
    if name!=None and stdPassword!=None:   
        st1=str(username)==str(name.Username)
        st2=str(stdPassword.Password)==str(password)
        if ( st1 and st2 ):
            return redirect(Home)
    else:
            status=True
            return render(request,'signin.html',{'status':status}) 

def viewAttendance(request,rollNo):
        student=Student.objects.filter(RollNo=rollNo)
        month=datetime.datetime.today().month
        attenadance = Attendance.objects.filter(date__icontains=month,student__RollNo=rollNo,status=True)
        count=len(attenadance)
        return HttpResponse(count)
    