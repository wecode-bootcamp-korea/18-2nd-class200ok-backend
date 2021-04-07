import json, jwt

from django.test import TransactionTestCase, Client

from unittest.mock import patch, MagicMock

from user.models    import User, Creator
from creator.views  import BasicInformationView
from lecture.models import (
                            Category, SubCategory, Difficulty,
                            Hashtag, PendingLecture, PendingLectureHashtag,
                            Introduction, Vote)

from my_settings import SECRET_KEY, HASHING_ALGORITHM

TEST_DATA = {
    "data" : {
    "sub_category_id" : "2",
    "detailed_category" : "손뜨개 코바늘",
    "difficulty" : "3"
    }
}


NONE_TEST_DATA = {
    "data" : {
    "sub_category_id" : None,
    "detailed_category" : None,
    "difficulty" : None
    }
}


USER_TEST_DATA = {
    "data" : {
    "username_id" : "1",
    "sub_category_id" : "2",
    "detailed_category" : "손뜨개 코바늘",
    "difficulty" : "3"
    }
}


class BasicInformationViewTest(TransactionTestCase):
    def setUp(self):
        User.objects.create(
            id = "1",
            username = "안다민",
            email = "damin0320@gmail.com",
            kakao_id = "1234567890"
        )
        
        self.token = jwt.encode({"username_id" : User.objects.get(id=1).id}, SECRET_KEY, algorithm=HASHING_ALGORITHM)
        
        PendingLecture.objects.create(
            title = "신나는 가죽공예",
            cover_image_url = "https://class2oo0k.s3.ap-northeast-2.amazonaws.com/media/misa.jpeg",
            summary_image_url = "https://class2oo0k.s3.ap-northeast-2.amazonaws.com/media/misa_note.jpeg",
        )
        
    def tearDown(self):
        User.objects.all().delete()
        PendingLecture.objects.all().delete()
        

    def test_basic_information_post_success(self):
        client = Client()
        header = {"HTTP_Authorization" : self.token}
        token = header["HTTP_Authorization"]
        payload = jwt.decode(token, SECRET_KEY, algorithms=HASHING_ALGORITHM)
        user = User.objects.get(id = payload["username_id"])
        response = client.post("/creator/basic-information", json.dumps(TEST_DATA), content_type="application/json", **header)
        self.assertEqual(response.status_code, 201)


    def test_basic_information_post_update(self):
        client = Client()
        header = {"HTTP_Authorization" : self.token}
        token = header["HTTP_Authorization"]
        payload = jwt.decode(token, SECRET_KEY, algorithms=HASHING_ALGORITHM)
        user = User.objects.get(id = payload["username_id"])
        response = client.post("/creator/basic-information", json.dumps(USER_TEST_DATA), content_type="application/json", **header)
        self.assertEqual(response.status_code, 201)
        
        
    def test_basic_information_post_token_fail(self):
        client = Client()
        header = {"NO_Authorization" : "1234"}
        response = client.post("/creator/basic-information", json.dumps(TEST_DATA), content_type="application/json", **header)
        self.assertEqual(response.status_code, 400)
        
        
    def test_basic_information_post_none_fail(self):
        client = Client()
        header = {"HTTP_Authorization" : self.token}
        token = header["HTTP_Authorization"]
        payload = jwt.decode(token, SECRET_KEY, algorithms=HASHING_ALGORITHM)
        user = User.objects.get(id = payload["username_id"])
        response = client.post("/creator/basic-information", json.dumps(NONE_TEST_DATA), content_type="application/json", **header)
        self.assertIsNotNone(response.status_code, 400)    