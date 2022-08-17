from user.models import CustomUser
from medical_inventory_site.settings import JWT_KEY
from rest_framework import exceptions, authentication
from django.utils import timezone
import datetime
import jwt

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token= authentication.get_authorization_header(request).decode()
        if not token:
            return None

        token=token.split()[1]
        try:
            payload=jwt.decode(token, key=JWT_KEY, algorithms=["HS256"], leeway=0, options={"verify_exp":"verify_signature", "verify_signature":True})
        except jwt.InvalidSignatureError:
            raise exceptions.AuthenticationFailed("Login Again, Invalid Token")
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Login Again, Token Expired")
        except (jwt.DecodeError, jwt.InvalidTokenError) as e:
            raise exceptions.AuthenticationFailed(e)
        
        try:
            user = CustomUser.objects.get(id=payload['user_id']) # get the user
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 

        return (user, payload) # authentication successful
    
    def generate_JWT(user):
        payload={
            "user_id":user.id,
            "email":user.email,
            "exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=60)
        }
        JWT_token=jwt.encode(
            payload=payload,
            key=JWT_KEY
        )
        return JWT_token