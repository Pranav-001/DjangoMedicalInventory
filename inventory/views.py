from rest_framework.decorators import api_view, authentication_classes, permission_classes
from user.custom_auth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Inventory
from .serializers import InventorySerializer


# Create your views here.
@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def select_all(request):
    inventories= Inventory.objects.all().order_by("seller")

    i=0
    dict_inventory={}
    for inventory in inventories:
        i+=1
        dict_inventory[("inventory {}".format(i))]={
            "inventory_id": inventory.id,
            "stock": inventory.stock,
            "shelf location": inventory.shelf_location, 
            "medicine": inventory.medicine.name, 
            "seller": inventory.seller.shop_name,
        }
    json_output={"user": dict_inventory}
    
    return Response(json_output)

@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def select_inventory(request, pk):
    inventories= Inventory.objects.filter(id=pk)
    i=0
    dict_inventory={}
    for inventory in inventories:
        i+=1
        dict_inventory[("inventory {}".format(i))]={
            "inventory_id": inventory.id,
            "stock": inventory.stock,
            "shelf location": inventory.shelf_location, 
            "medicine": inventory.medicine.name, 
            "seller": inventory.seller.shop_name,
        }
    json_output={"user": dict_inventory}

    return Response(json_output)
    

@api_view(['POST'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def insert_inventory(request):
    data_insert=request.data
    data_insert["created_by"]=request.user.id

    data_serial=InventorySerializer(data=data_insert)
    if not data_serial.is_valid():
        return Response(data_serial.errors)
    
    Inventory.objects.create(**data_serial.validated_data)
    return Response({"Inventory": "Record Created"})