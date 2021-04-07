import json, bcrypt, jwt, boto3, os, logging, uuid
from json import JSONDecodeError


from django.views import View
from django.http  import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


from my_settings            import AWS_STORAGE_BUCKET_NAME
from creator.custom_storage import MediaStorage


from lecture.models import (
                            Category, SubCategory, Difficulty,
                            Hashtag, PendingLecture, PendingLectureHashtag,
                            Introduction, Vote)
from user.models    import User, Creator

from utils.decorators import auth_check


class BasicInformationView(View):
    @auth_check
    def post(self,request):
        try:
            data = json.loads(request.body)
            sub_category_id = data.get('sub_category_id')
            detailed_category = data.get('detailed_category')
            difficulty_id = data.get('difficulty_id')

            if not PendingLecture.objects.filter(user=request.user).exists():
                PendingLecture.objects.create(
                        sub_category_id = sub_category_id,
                        detailed_category = detailed_category,
                        difficulty_id = difficulty_id,
                    )
            else:
                PendingLecture.objects.filter(user=request.user).update(                                                
                        sub_category_id = sub_category_id,
                        detailed_category = detailed_category,
                        difficulty_id = difficulty_id,
                    )         
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'message': 'TYPE_ERROR'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'message' : 'USER_DOES_NOT_EXIST'}, status=400)