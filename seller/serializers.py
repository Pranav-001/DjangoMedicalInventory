from django.core.exceptions import ValidationError
from rest_framework import serializers
from user.models import CustomUser

from .models import Seller


class SellerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Seller
		fields = ('shop_name', 'location', 'created_on', 'created_by', 'user')


class UpdateSellerSerializer(serializers.ModelSerializer):
	shop_name = serializers.CharField(max_length=255),
	location = serializers.CharField(max_length=255),       
	user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
	
	class Meta:
		model = Seller
		fields = ('shop_name', 'location', 'updated_by', 'user')


	def is_valid(self, raise_exception=False):
		if hasattr(self, 'initial_data'):
			payload_keys = self.initial_data.keys() # all the payload keys
			serializer_fields = self.fields.keys() # all the serializer fields
			extra_fields = filter(lambda key: key not in serializer_fields , payload_keys) 
			if extra_fields:
				raise ValidationError('Extra fields %s in payload'%extra_fields)
		return super(UpdateSellerSerializer, self).is_valid(raise_exception)
