from rest_framework import serializers
from .models import Medicine, ChemicalCompound

class MedicineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medicine
		fields = ('name', 'max_price', 'usage', 'dose', 'prescription', 'max_selling_quantity', 'company', 'chemical_compound', 'created_by', 'updated_by')

class UpdateMedicineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medicine
		fields = ('name', 'max_price', 'usage', 'dose', 'prescription', 'max_selling_quantity', 'company', 'chemical_compound', 'updated_by')
        
class ChemicalCompoundSerializer(serializers.ModelSerializer):
	class Meta:
		model = ChemicalCompound
		fields = ('name', 'created_by', 'updated_by')

class UpdateChemicalCompoundSerializer(serializers.ModelSerializer):
	class Meta:
		model = ChemicalCompound
		fields = ('name', 'updated_by')


class SimpleChemicalCompoundSerializer(serializers.ModelSerializer):
	name= serializers.CharField(required= True, max_length=255)
	class Meta:
		model = ChemicalCompound
		fields = ('name', 'created_by', 'updated_by')