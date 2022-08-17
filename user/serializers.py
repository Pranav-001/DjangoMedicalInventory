import email
from rest_framework import serializers
from .models import CustomUser


class SignupSerializer(serializers.ModelSerializer):
	
	class Meta: #read more about it
		model = CustomUser
		fields = ("email", "phone_number", "password", "first_name", "last_name")

class LoginSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=128, required=True)
	email = serializers.EmailField(max_length=255, required=True)
	class Meta:
		model = CustomUser
		fields = ("email", "password")

class UpdateSerializer(serializers.ModelSerializer):
	phone_number= serializers.CharField(max_length=10, required=False)
	email= serializers.CharField(max_length=255, required=False)
	password= serializers.CharField(max_length=128, required= False)
	class Meta:
		model = CustomUser
		fields = ("email", "phone_number", "password", "first_name", "last_name")