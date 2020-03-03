from rest_framework import serializers
from .models import *

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=('student','date','status')
        depth=1



