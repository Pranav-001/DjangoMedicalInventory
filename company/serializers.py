from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ('name', 'created_by')

class UpdateCompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ('name', 'updated_by')

class SimpleCompanySerializer(serializers.ModelSerializer):
	name=serializers.CharField(required=True, max_length=255)
	class Meta:
		model = Company
		fields = ('name', 'created_by')