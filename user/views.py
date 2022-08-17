from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from user.custom_auth import CustomAuthentication
from .serializers import SignupSerializer, LoginSerializer, UpdateSerializer
from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

# Create your views here.
@api_view(['POST'])
@authentication_classes((CustomAuthentication,))
@permission_classes((AllowAny,))
def signup(request):
    user_data=request.data

    if not user_data['password']==user_data['repeat_password']:
        return Response({'Error' : 'passwords don\'t match.'})
    
    user_data.pop("repeat_password")

    user_serial = SignupSerializer(data=user_data)
    if user_serial.is_valid():
        user_serial.validated_data['password']=make_password(user_serial.validated_data['password'])
        user= CustomUser.objects.create(**user_serial.validated_data)
        output= Response({"user": "Record Created"})
    else:
        output= Response(user_serial.errors)
   
    return output

@api_view(['POST'])
@authentication_classes((CustomAuthentication,))
@permission_classes((AllowAny,))
def login(request):
    
    user_serial=LoginSerializer(data=request.data)
    if not user_serial.is_valid():
        return Response(user_serial.errors)

    if not CustomUser.objects.filter(email=user_serial.initial_data['email']):
        return Response({'Error' : 'Invalid Username (email).'})  

    user=CustomUser.objects.get(email=user_serial.validated_data['email'])
    if not check_password(user_serial.validated_data['password'], user.password):
        return Response({'Error' : 'Invalid password.'})

    user.last_login=timezone.now()
    if not user.is_active:
        user.is_active=True
    user.save()
    JWT_token=CustomAuthentication.generate_JWT(user)
    return Response({
        "Login": "successfull",
        "Token": JWT_token
    })

@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAdminUser,))
def select_all(request): 
    users= CustomUser.objects.filter(is_active=True)
    i=0
    dict_user={}
    for user in users:
        i+=1
        dict_user[("user {}".format(i))]={
            "User_id": user.id,
            "Email": user.email,
            "First Name": user.first_name
        }
    json_output={"user": dict_user}
    
    return Response(json_output)

@api_view(['GET'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def select_user(request, pk): 
    if request.user.is_staff:
        users= CustomUser.objects.filter(id=pk, is_active=True)
    else:
        users= CustomUser.objects.filter(id=request.user.id, is_active=True)
    if not users:
        return Response({"user": "No Record"})

    i=0
    dict_user={}
    for user in users:
        i+=1
        dict_user[("user {}".format(i))]={
            "User_id": user.id,
            "Email": user.email,
            "First Name": user.first_name
        }
    json_output={"user": dict_user}
    
    return Response(json_output)

@api_view(['DELETE'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def delete_user(request, pk): #need to make it better
    if request.user.is_staff:
        users= CustomUser.objects.filter(id=pk, is_active=True)
    else:
        users= CustomUser.objects.filter(id=request.user.id, is_active=True)
    if not users:
        return Response({"user": "No Record"})

    CustomUser.objects.filter(id=pk).update(is_active=False)
    
    return Response({"user": "Deactivated"})
   
@api_view(['PUT'])
@authentication_classes((CustomAuthentication,))
@permission_classes((IsAuthenticated,))
def update_user(request, pk):
    if request.user.is_staff:
        users= CustomUser.objects.filter(id=pk, is_active=True)
    else:
        users= CustomUser.objects.filter(id=request.user.id, is_active=True)
    if not users:
        return Response({"user": "No Record"})
    
    data_serial=UpdateSerializer(data= request.data)
    if not data_serial.is_valid():
        return Response(data_serial.errors)

    if "password" in data_serial.validated_data:
        data_serial.validated_data['password']=make_password(data_serial.validated_data['password'])
    
    CustomUser.objects.filter(id=pk).update(**data_serial.validated_data)

    return Response({"user": "Record Updated"})
