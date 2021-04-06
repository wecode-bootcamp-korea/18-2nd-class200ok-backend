import json

from datetime import datetime, timedelta

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q, Count

from user.models import User
from .models     import (
    SubCategory,
    Difficulty,
    PendingLecture,
    Introduction,
    Vote
)

class PendingLectureListView(View):
    def get(self,request):

        sub_categories  = request.GET.getlist('sub_category', None)
        sort            = request.GET.get('sort', 'latest')

        # 쿼리스트링으로 같은 변수 여러개-> getlist
        q = Q()
        if sub_categories:
            for sub_category in sub_categories:
                q.add(Q(sub_category=sub_category), q.OR)

        # 최신순,인기순
        sort_options = {
            'latest'  : '-created_at',
            'popular' : '-count'
        }
        
        # 필터링 한것 중 솔팅
        pending_classes = PendingLecture.objects.filter(q).annotate(count=Count('vote')).order_by(sort_options[sort])

        pending_classes = [{
            'id'           : pending_class.id,
            'cover_image'  : pending_class.cover_image_url,
            'category'     : pending_class.sub_category.name,
            'creator'      : pending_class.user.username,
            'title'        : pending_class.title,
            'achieve_rate' : int((pending_class.count/20)*100),
            'due_date'     : int((pending_class.created_at.replace(tzinfo=None)-datetime.now()).days)+15,
        } for pending_class in pending_classes]
        return JsonResponse({'pending_classes' : pending_classes}, status=200)
