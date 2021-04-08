import json, bcrypt, jwt, boto3, os, logging, uuid
from json import JSONDecodeError

from django.views import View
from django.http  import JsonResponse
from django.db    import transaction, IntegrityError

from my_settings            import AWS_STORAGE_BUCKET_NAME
from creator.custom_storage import MediaStorage
from lecture.models         import (
                            Category, SubCategory, Difficulty,
                            Hashtag, PendingLecture, PendingLectureHashtag,
                            Introduction, Vote)
from user.models            import User, Creator
from utils.decorators       import auth_check


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

class TitleAndCoverView(View):
    @auth_check
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            file_obj = request.FILES.get('cover_image')
            title = request.POST.get('title')

            file_name = file_obj.name
            file_path_within_bucket = str(uuid.uuid4()) + file_name

            media_storage = MediaStorage()
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)
            PendingLecture.objects.filter(user=user).update(cover_image_url=file_url, title=title)
            
            return JsonResponse({'result' : 'Title and cover image uploaded'}, status=201)
        
        except AttributeError:
            return JsonResponse({"message": "Attribute_Error, possibly image not received"}, status=400)
        except PendingLecture.DoesNotExist:
            return JsonResponse({"message": "Please submit basic information from https://class101.net/creators/compact/edit/hZr6aB03qCE6JCGuXIjv/basic-information"}, status=403)


class ClassIntroductionView(View):
    @auth_check
    def post(self, request):
        try: 
            user = request.user
            pending_lecture = PendingLecture.objects.get(user=user)
            file_objs = request.FILES.getlist('introduction_image')

            for i in range(len(file_objs)):
                file_name = file_objs[i].name
                file_path_within_bucket = str(uuid.uuid4()) + file_name

                media_storage = MediaStorage()
                media_storage.save(file_path_within_bucket, file_objs[i])
                file_url = media_storage.url(file_path_within_bucket)
                Introduction.objects.create(image_url=file_url, pending_lecture=pending_lecture)
            return JsonResponse({'result' : 'Introduction image(s) and detail(s) uploaded'}, status=201)
        
        except AttributeError:
            return JsonResponse({"message": "Attribute_Error, possibly image not received"}, status=400)
        except PendingLecture.DoesNotExist:
            return JsonResponse({"message": "Please submit basic information from https://class101.net/creators/compact/edit/hZr6aB03qCE6JCGuXIjv/basic-information"}, status=403)


class SummaryView(View):
    @auth_check
    def post(self, request):
        try:
            user = request.user
            pending_lecture = PendingLecture.objects.get(user=user)
            file_obj = request.FILES.get('summary_image')
            tags = request.POST.getlist('tag')

            file_name = file_obj.name
            file_path_within_bucket = str(uuid.uuid4()) + file_name

            media_storage = MediaStorage()
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)
            PendingLecture.objects.filter(user=user).update(summary_image_url=file_url)

            for tag in tags:
                if Hashtag.objects.filter(tag=tag).exists():
                    hashtag=Hashtag.objects.get(tag=tag)
                    if PendingLectureHashtag.objects.filter(pending_lecture=pending_lecture, hashtag=hashtag).exists():
                        pass
                    else:
                        PendingLectureHashtag.objects.create(pending_lecture=pending_lecture, hashtag=hashtag)
                else:
                    hashtag=Hashtag.objects.create(tag=tag)
                    PendingLectureHashtag.objects.create(pending_lecture=pending_lecture, hashtag=hashtag)

            return JsonResponse({'result' : 'Summary and tag(s) uploaded'}, status=201)
        
        except AttributeError:
            return JsonResponse({"message": "Attribute_Error, possibly image not received"}, status=400)
        except PendingLecture.DoesNotExist:
            return JsonResponse({"message": "Please submit basic information from https://class101.net/creators/compact/edit/hZr6aB03qCE6JCGuXIjv/basic-information"}, status=403)


class CreatorIntroductionView(View):
    @auth_check
    def post(self, request):
        try:            
            user = request.user
            pending_lecture = PendingLecture.objects.get(user=user)
            file_obj = request.FILES.get('profile_image')
            data = request.POST
            nickname = data.get('nickname')
            phonenumber = data.get('phonenumber')
            introduction = data.get('introduction')

            file_name = file_obj.name
            file_path_within_bucket = str(uuid.uuid4()) + file_name

            media_storage = MediaStorage()
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)

            if Creator.objects.filter(user=user).exists():
                Creator.objects.filter(user=user).update(nickname=nickname, phonenumber=phonenumber, introduction=introduction, profile_image_url=file_url)
                return JsonResponse({'result' : 'Creator profile updated'}, status=201)
            else:
                Creator.objects.create(nickname=nickname, phonenumber=phonenumber, introduction=introduction, profile_image_url=file_url)
                return JsonResponse({'result' : 'Creator profile uploaded'}, status=201)

        except AttributeError:
            return JsonResponse({"message": "Attribute_Error, possibly image not received"}, status=400)
        except IntegrityError:
            return JsonResponse({"message": "IntegrityError, possibly duplicated entry for key 'nickname' or 'phonenumber'"}, status=400)
        except PendingLecture.DoesNotExist:
            return JsonResponse({"message": "Please submit basic information from https://class101.net/creators/compact/edit/hZr6aB03qCE6JCGuXIjv/basic-information"}, status=403)
