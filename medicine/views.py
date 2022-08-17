from .serializers import MedicineSerializer, ChemicalCompoundSerializer, SimpleChemicalCompoundSerializer, UpdateMedicineSerializer, UpdateChemicalCompoundSerializer
from .models import Medicine, ChemicalCompound
from company.serializers import SimpleCompanySerializer
from company.models import Company
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from user.custom_auth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import exceptions


# Create your views here.

#chemcical Compound

@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def select_all_chemical_compound(request):    
    chemical_compounds= ChemicalCompound.objects.all().order_by("id")
    dict_chemical_compound={}
    output=[]
    for chemical_compound in chemical_compounds:
        dict_chemical_compound["chemical_compound"]={
            "chemical_compound_id": chemical_compound.id,
            "name": chemical_compound.name,
        }
    output+=(dict_chemical_compound,)
    
    return Response(output)

@api_view(['POST'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def insert_chemical_compound(request):

    insert_data=request.data
    insert_data["created_by"]=request.user.id

    insert_serial=ChemicalCompoundSerializer(data=insert_data)
    if not insert_serial.is_valid():
        return Response(insert_serial.errors)
    
    ChemicalCompound.objects.create(**insert_serial.validated_data)
    return Response({"chemical compound": "Record Created"}, status=201)

@api_view(['DELETE'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def delete_chemical_compound(request, pk):
    ChemicalCompound.objects.filter(id=pk).delete()
    return Response({"Chemical Compound": "Record Deleted"})

@api_view(['PUT'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def update_chemical_compound(request, pk):
    try:
        chemical_compound=ChemicalCompound.objects.get(id=pk)
    except ChemicalCompound.DoesNotExist:
        raise exceptions.AuthenticationFailed('No such record')

    insert_data=request.data
    insert_data["updated_by"]=request.user.id

    insert_serial=UpdateChemicalCompoundSerializer(data=insert_data)
    if not insert_serial.is_valid():
        return Response(insert_serial.errors)
    
    chemical_compound.update(**insert_serial.validated_data)

    return Response({"Chemical Compound": "Record Updated"})

@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def select_chemical_compound(request, pk):
    try:
        chemical_compound=ChemicalCompound.objects.get(id=pk)
    except ChemicalCompound.DoesNotExist:
        raise exceptions.AuthenticationFailed('No such record')
    dict_chemical_compound={}
    output=[]
    dict_chemical_compound["chemical_compound"]={
        "chemical_compound_id": chemical_compound.id,
        "name": chemical_compound.name,
    }
    output+=(dict_chemical_compound, )
    
    return Response(output)

#Medicine

@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def select_all_medicine(request):    
    medicines= Medicine.objects.all().order_by("id")
    dict_medicine={}
    output=[]
    for medicine in medicines:
        dict_medicine["medicine"]={
            "medicine_id": medicine.id,
            "name": medicine.name,
            "max_price": medicine.max_price, 
            "dose": medicine.dose, 
            "prescription": medicine.prescription,
            "max_selling_quantity": medicine.max_selling_quantity,
            "chemical_compound": medicine.chemical_compound.name,
            "company": medicine.company.name,
        }
    output+=(dict_medicine, )
    
    return Response(output)

@api_view(['POST'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def insert_medicine(request):
    insert_data=request.data
  
    chemical_compound_data={}
    chemical_compound_data["name"]=insert_data["chemical_compound"]
    chemical_compound_data["created_by"]=request.user.id
    insert_serial=SimpleChemicalCompoundSerializer(data=chemical_compound_data)
    if not insert_serial.is_valid():
        return Response(insert_serial.errors)
    chemical_compund, created=ChemicalCompound.objects.get_or_create( name= insert_serial.validated_data["name"], defaults= {"created_by": insert_serial.validated_data["created_by"]})

    insert_data["chemical_compound"]=chemical_compund.id

    company_data={}
    company_data["name"]=insert_data["company"]
    company_data["created_by"]=request.user.id
    insert_serial=SimpleCompanySerializer(data=company_data)
    if not insert_serial.is_valid():
        return Response(insert_serial.errors)
    company, created=Company.objects.get_or_create( name= insert_serial.validated_data["name"], defaults= {"created_by": insert_serial.validated_data["created_by"]})
    print(company, print)
    insert_data["company"]=company.id   

    insert_data["created_by"]=request.user.id

    insert_serial=MedicineSerializer(data=insert_data)
    if not insert_serial.is_valid():
        return Response(insert_serial.errors)
    
    Medicine.objects.create(**insert_serial.validated_data)
    return Response({"Medicine": "Record Created"}, status=201)

@api_view(['DELETE'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def delete_medicine(request, pk):
    Medicine.objects.filter(id=pk).delete()
    return Response({"Medicine": "Record Deleted"})

@api_view(['PUT'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def update_medicine(request, pk):
    try:
        medicine= Medicine.objects.get(id=pk)
    except Company.DoesNotExist:
        raise exceptions.AuthenticationFailed('No such record')
    
    insert_data=request.data
  
    if "chemical_compound" in insert_data:
        chemical_compound_data={}
        chemical_compound_data["name"]=insert_data["chemical_compound"]
        chemical_compound_data["created_by"]=request.user.id
        insert_serial=SimpleChemicalCompoundSerializer(data=chemical_compound_data)
        if not insert_serial.is_valid():
            return Response(insert_serial.errors)
        chemical_compund, created=ChemicalCompound.objects.get_or_create( name= insert_serial.validated_data["name"], defaults= {"created_by": insert_serial.validated_data["created_by"]})

        insert_data["chemical_compound"]=chemical_compund.id

    if "company" in insert_data:
        company_data={}
        company_data["name"]=insert_data["company"]
        company_data["created_by"]=request.user.id
        insert_serial=SimpleCompanySerializer(data=company_data)
        if not insert_serial.is_valid():
            return Response(insert_serial.errors)
        company, created=Company.objects.get_or_create( name= insert_serial.validated_data["name"], defaults= {"created_by": insert_serial.validated_data["created_by"]})
        print(company, print)
        insert_data["company"]=company.id   

        insert_data["updated_by"]=request.user.id

    insert_serial=UpdateMedicineSerializer(data=insert_data)
    if not insert_serial.is_valid():
        return Response(insert_serial.errors)
    
    medicine.update(**insert_serial.validated_data)
    return Response({"Medicine": "Record Updates"})

@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def select_medicine(request, pk):
    try:
        medicine= Medicine.objects.get(id= pk)
    except Company.DoesNotExist:
        raise exceptions.AuthenticationFailed('No such record')

    dict_medicine={}
    output=[]
    dict_medicine["medicine"]={
        "medicine_id": medicine.id,
        "name": medicine.name,
        "max_price": medicine.max_price, 
        "dose": medicine.dose, 
        "prescription": medicine.prescription,
        "max_selling_quantity": medicine.max_selling_quantity,
        "chemical_compound": medicine.chemical_compound.name,
        "company": medicine.company.name,
    }
    output=(dict_medicine, )
    
    return Response(output)