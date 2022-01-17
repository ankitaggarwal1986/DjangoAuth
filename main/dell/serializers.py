from rest_framework import serializers
from . models import Employee, Tracking
from django.db.models import fields
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]

    def create(self, validated_data):
         user = User.objects.create(username = validated_data['username'])
         user.set_password(validated_data['password'])
         user.save()
         return user     

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = "__all__"



