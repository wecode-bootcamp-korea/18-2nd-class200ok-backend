from django.shortcuts import render

# Create your views here.
import json
import bcrypt
import jwt
import requests

from django.shortcuts       import redirect
from django.views           import View
from django.http            import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db              import IntegrityError

from my_settings import SECRET_KEY, HASHING_ALGORITHM
from .models     import User, Creator


class KakaoSignInView(View):
    def post(self,request):
        try:
            access_token = request.headers.get('Authorization')
            user_profile = requests.get(
                'https://kapi.kakao.com//v2/user/me', 
                headers={'Authorization' : 'Bearer {}'.format(access_token)}
                )
            json_user_profile = user_profile.json()
            kakao_id   = json_user_profile['id']
            nickname   = json_user_profile['properties']['nickname']
            user_email = json_user_profile['kakao_account']['email']
            if not User.objects.filter(kakao_id = kakao_id): 
                username = User.objects.create(
                    username = nickname,
                    email    = user_email,
                    kakao_id = kakao_id
                )
                new_token = jwt.encode({'username_id' : username.id}, SECRET_KEY, algorithm=HASHING_ALGORITHM)
                return JsonResponse({'message' : "SIGN_IN_SUCCESS",'new_token' : new_token},status=200)
            username = User.objects.get(kakao_id=kakao_id)
            new_token = jwt.encode({'username_id' : username.id}, SECRET_KEY, algorithm=HASHING_ALGORITHM)
            return JsonResponse({'message' : "LOGIN_SUCCESS", 'new_token' : new_token}, status=200)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({"message" : "USER_DOES_NOT_EXIST"}, status=400)




