import json, bcrypt, jwt, boto3, os, logging, uuid
from django.views     import View
from django.http      import JsonResponse

from user.models import *
from lecture.models import *
from my_settings    import AWS_STORAGE_BUCKET_NAME
from creator.custom_storage import MediaStorage

class BasicInformationView(View):
    def post(self, request, **kwargs):
        return

class TitleAndCoverView(View):
    def post(self, request, **kwargs):
        return

class ClassIntroduction(View):
    def post(self, request, **kwargs):
        return

class SummaryView(View):
    def post(self, request, **kwargs):
        return
        
class CreatorIntroductionView(View):
    def post(self, request, **kwargs):
        return

class FinalChecklistsView(View):
    def post(self, request, **kwargs):
        return