import json
import jwt
from jwt.exceptions import InvalidSignatureError, DecodeError


from django.http import JsonResponse


from user.models import User, Creator
from my_settings import SECRET_KEY, HASHING_ALGORITHM


# auth check with blocking
def auth_check(func):
    def wrapper(self, request):
        try:
            new_token = request.headers.get('Authorization')
            if not new_token:
                return JsonResponse({'message' : 'TOKEN_DOES_NOT_EXIST'}, status=400)
            
            decoded_auth_token = jwt.decode(new_token, SECRET_KEY, algorithms=HASHING_ALGORITHM)
            username_id = decoded_auth_token['username_id']
            user = User.objects.get(id=username_id)
            
            request.user = user
            return func(self, request)

        except InvalidSignatureError:
            return JsonResponse({'message': 'SIGNATURE_VERIFICATION_FAILED'}, status=400)
        except DecodeError:
            return JsonResponse({'message': 'DECODE_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'USER_DOES_NOT_EXIST'}, status=404)
    return wrapper

# user check without blocking
def user_check(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            new_token = request.headers.get('Authorization')
            if not new_token:
                request.user = None
                return func(self, request, *args, **kwargs)
            decoded_auth_token = jwt.decode(new_token, SECRET_KEY, algorithms=HASHING_ALGORITHM)
            
            user_id = decoded_auth_token['user_id']
            user = User.objects.get(id=user_id)
            
            request.user = user
            return func(self, request)

        except InvalidSignatureError:
            return JsonResponse({'message': 'SIGNATURE_VERIFICATION_FAILED'}, status=400)
        except DecodeError:
            return JsonResponse({'message': 'DECODE_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'USER_DOES_NOT_EXIST'}, status=404)
    return wrapper