import json

from django.test import TestCase, Client

from user.models import User

from .models import (
    Category,
    SubCategory,
    Difficulty,
    Hashtag,
    PendingLecture,
    PendingLectureHashtag,
    Introduction,
    Vote
)

class PendingLectureDetailTest(TestCase):
    def setUp(self):
        User.objects.create(
            id       = 1,
            username = '박효신',
            email    = 'parkhyoshin@wemail.com',
            kakao_id = '1111111111'
        )
        Category.objects.create(
            id   = 1, 
            name = '취미'
        )
        SubCategory.objects.create(
            id          = 1, 
            name        = '미술', 
            category_id = 1
        )
        Difficulty.objects.create(
            id    = 1,
            level = '입문자'
        )
        Hashtag.objects.create(
            id  = 1,
            tag = '잘생겼다'
        )
        PendingLecture.objects.create(
            id                = 1,
            title             = '자화상 그리기',  
            cover_image_url   = 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg', 
            summary_image_url = 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg',
            detailed_category = '취미 그림',
            user_id           = 1,
            category_id       = 1,
            sub_category_id   = 1,
            difficulty_id     = 1,
        )
        PendingLectureHashtag.objects.create(
            pending_lecture_id = 1,
            hashtag_id         = 1,
        )
        Introduction.objects.create(
            id                 = 1,
            detail             = '후후 어렵지',
            image_url          = 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg', 
            pending_lecture_id = 1
        )
        Introduction.objects.create(
            id                 = 2,
            detail             = '당연히 어렵지',
            image_url          = 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg', 
            pending_lecture_id = 1
        )
        Introduction.objects.create(
            id                 = 3,
            detail             = '원래 어려워',
            image_url          = 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg', 
            pending_lecture_id = 1
        )
        Vote.objects.create(
            id                 = 1,
            user_id            = 1,
            pending_lecture_id = 1,
        )

    def tearDown(self):
        User.objects.all().delete()
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        Difficulty.objects.all().delete()
        Hashtag.objects.all().delete()
        PendingLecture.objects.all().delete()
        PendingLectureHashtag.objects.all().delete()
        Introduction.objects.all().delete()
        Vote.objects.all().delete()


    def test_pendinglecture_detail_get_success(self):
        pending_lecture_id = 1
        client    = Client()
        response  = client.get(f'/lecture/{pending_lecture_id}')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                "pending_lecture": {
                "lecture_id": 1,
                "title": '자화상 그리기',
                "images": [
            {
                "id": 1,
                "image_url": 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg',
                "detail": '후후 어렵지',
                "tags": [
                    "by.박효신",
                    '미술',
                    '취미 그림',
                    "입문자"
                ]
            },
            {
                "id": 2,
                "image_url": 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg',
                "detail": '당연히 어렵지',
                "tags" : ['잘생겼다']
            },
            {
                "id": 3,
                "image_url": 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg',
                "detail": '원래 어려워'
            }
        ]
    }
}
        )

    def test_pendinglecture_detail_get_fail(self):
        pending_lecture_id = 2
        client   = Client()
        response = client.get(f'/lecture/{pending_lecture_id}')
        Vote.objects.all().delete()

class PendingLectureListTest(TestCase):
    def setUp(self):
        User.objects.create(
            id       = 1,
            username = '박효신',
            email    = 'parkhyoshin@wemail.com',
            kakao_id = '1111111111'
        )
        Category.objects.create(
            id   = 1, 
            name = '취미'
        )
        SubCategory.objects.create(
            id          = 1, 
            name        = '미술', 
            category_id = 1
        )
        Difficulty.objects.create(
            id    = 1,
            level = '입문자'
        )
        Hashtag.objects.create(
            id  = 1,
            tag = '잘생겼다'
        )
        PendingLecture.objects.create(
            id                = 1,
            title             = '자화상 그리기',  
            cover_image_url   = 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg', 
            summary_image_url = 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg',
            detailed_category = '취미 그림',
            user_id           = 1,
            category_id       = 1,
            sub_category_id   = 1,
            difficulty_id     = 1,
        )
        PendingLectureHashtag.objects.create(
            pending_lecture_id = 1,
            hashtag_id         = 1,
        )
        Introduction.objects.create(
            id                 = 1,
            detail             = '후후 어렵지',
            image_url          = 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/06/28/96228163.2.jpg', 
            pending_lecture_id = 1
        )

    def tearDown(self):
        User.objects.all().delete()
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        Difficulty.objects.all().delete()
        Hashtag.objects.all().delete()
        PendingLecture.objects.all().delete()
        PendingLectureHashtag.objects.all().delete()
        Introduction.objects.all().delete()


    def test_pendinglecture_list_get(self):
        client    = Client()
        response  = client.get('/lecture')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['pending_classes'][0]['id'],1)

    def test_pendinglecture_list_not_found(self):
        client = Client()
        response=client.get('/lectures')

        self.assertEqual(response.status_code,404)
