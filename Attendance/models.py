from django.db import models

class Admin(models.Model):
    Username = models.CharField(max_length=30,primary_key=True,unique=True)
    Name = models.CharField(max_length=30)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)



class Student(models.Model):
    RollNo = models.CharField(max_length=30, primary_key=True, unique=True)
    StdName = models.CharField(max_length=30)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)


class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.BooleanField(default=False)