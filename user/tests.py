import json, jwt

from django.test    import TransactionTestCase, Client

from unittest.mock  import patch, MagicMock

from user.models import User

from my_settings import SECRET_KEY, HASHING_ALGORITHM

class KakaoLoginTest(TransactionTestCase):    
    def setUp(self):
        User.objects.create(
            id = 1,
            username = '안다민',
            kakao_id = '1234567890',
            email = 'damin0320@kakao.com'
        )

        self.token = jwt.encode({'username_id' : User.objects.get(id=1).id}, SECRET_KEY, algorithm=HASHING_ALGORITHM)    
        
    def tearDown(self):
        User.objects.all().delete()
        
    @patch('user.views.requests')
    def test_kakao_login_success(self, mocked_requests):
        client = Client()
        class MockedResponse:
            def json(self):
                return {
                    "id" : "1234567890",
                    "properties" : {
                        "nickname" : "안다민"
                    },
                    "kakao_account" : {
                        "email" : "damin0320@kakao.com"
                    }
                }
        mocked_requests.get = MagicMock(return_value=MockedResponse())
        
        header = {'HTTP_Authorization' : self.token}
        response = client.post('/user/signin', content_type='application/json', **header)
        self.assertEqual(response.status_code, 200)
        
   
    def test_kakao_login_fail(self):
        client   = Client()
        header   = {'No_Authorizaeion' : '1234'}
        response = client.post('/user/signin', content_type='application/json', **header)
        self.assertEqual(response.status_code, 400)        