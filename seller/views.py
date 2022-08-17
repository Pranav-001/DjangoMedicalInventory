from functools import partial

from rest_framework import exceptions
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from user.custom_auth import CustomAuthentication

from .models import Seller
from .serializers import SellerSerializer, UpdateSellerSerializer


# Create your views here.
@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def select_all(request):

    try:

        if request.user.is_staff:
            sellers= Seller.objects.all().order_by("id")
        else:
            sellers= Seller.objects.filter(user=request.user.id).order_by(id)    

    except Seller.DoesNotExist:

        raise exceptions.AuthenticationFailed('No such record')


    dict_seller={}
    output=[]

    for seller in sellers:

        dict_seller["seller"]={
            "seller_id": seller.id,
            "location": seller.location,
            "shop name": seller.shop_name, 
            "user": seller.user.email, 
        }


    output+=(dict_seller, ) 
    return Response(output)

@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def select_seller(request, pk):

    try:

        if request.user.is_staff:
            seller= Seller.objects.get(id= pk)
        else:
            seller= Seller.objects.get(id= pk, user=request.user.id)

    except Seller.DoesNotExist:

        raise exceptions.AuthenticationFailed('No such record')


    dict_seller={}
    output=[]
   
    dict_seller["seller"]={
        "seller_id": seller.id,
        "location": seller.location,
        "shop name": seller.shop_name, 
        "user": seller.user.email, 
    }

    output+=(dict_seller, )
    return Response(output)

@api_view(['DELETE'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def delete_seller(request, pk):

    if request.user.is_staff:
        Seller.objects.filter(id=pk).delete()

    else:
        Seller.objects.filter(id=pk, user=request.user.id).delete()


    return Response({"Seller": "Record Deleted"})

@api_view(['POST'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def signup(request):

    insert_data= request.data
    insert_data["created_by"]=request.user.id

    serial_data=SellerSerializer(data=insert_data)

    if not serial_data.is_valid():
        return Response(serial_data.errors)
    
    Seller.objects.create(**serial_data.validated_data)

    return Response({"Seller": "Record Created"}, status=201)


@api_view(['PATCH'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def update_seller(request, pk):
    
    if request.user.is_staff:
        seller= Seller.objects.filter(id=pk)
    else:
        seller= Seller.objects.filter(id=pk, user=request.user.id)
    if not seller:
        return Response({"Seller": "No Record/ No Access"})
    
    insert_data= request.data
    insert_data["updated_by"]=request.user.id

    serial_data=UpdateSellerSerializer(data=insert_data, partial=True)
    print(serial_data)
    if not serial_data.is_valid():
        return Response(serial_data.errors)
    
    Seller.objects.get(id=pk).update(**serial_data.validated_data)
    return Response({"Seller": "Record Created"})
