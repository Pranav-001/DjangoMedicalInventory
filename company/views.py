from rest_framework import authentication, exceptions
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from user.custom_auth import CustomAuthentication

from .models import Company
from .serializers import CompanySerializer, UpdateCompanySerializer


# Create your views here.
@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def select_all(request):
    companys= Company.objects.all().order_by("name")
    dict_company={}
    output=[]
    for company in companys:
        dict_company["company"]={
            "company_id": company.id,
            "name": company.name,
        }
        output+=(dict_company,)
    
    return Response(output)

@api_view(['POST'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def insert(request):
    insert_data=request.data
    insert_data["created_by"]=request.user.id

    insert_serial=CompanySerializer(data=insert_data)
    if not insert_serial.is_valid():
        return Response(insert_serial.errors)
    
    company= Company.objects.create(**insert_serial.validated_data)
    return Response({"Company record Created"}, status=201)

@api_view(['DELETE'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def delete(request, pk):
    Company.objects.filter(id=pk).delete()
    return Response({"Company": "Record Deleted"})

@api_view(['PUT'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def update(request, pk):
    try:
        company= Company.objects.get(id=pk)
    except Company.DoesNotExist:
        raise exceptions.AuthenticationFailed("No such record")
    

    insert_data=request.data
    insert_data["updated_by"]=request.user.id

    insert_serial=UpdateCompanySerializer(data=insert_data)
    if not insert_serial.is_valid():
        return Response(insert_serial.errors)
    
    company.update(**insert_serial.validated_data)

    return Response({"Company": "Record Updated"})

@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def select(request, pk):
    try:
        company= Company.objects.get(id= pk)
    except Company.DoesNotExist:
        raise exceptions.AuthenticationFailed('No such record')
    dict_company={}
    dict_company["company"]={
        "company_id": company.id,
        "name": company.name,
    }
    output=(dict_company,)
    return Response(output)
