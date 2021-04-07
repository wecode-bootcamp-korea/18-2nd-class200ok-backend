import json

from django.test    import TransactionTestCase, Client

from unittest.mock  import patch, MagicMock

from user.models import User


class KakaoLoginTest(TransactionTestCase):    
    def setUp(self):
        User.objects.create(
            username = '안다민',
            kakao_id = '1234567890',
            email = 'damin0320@kakao.com'
        )
        
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
        
        header = {'HTTP_Authorization' : 'access_token'}
        response = client.post('/user/signin', content_type='application/json', **header)
        self.assertEqual(response.status_code, 200)
        
   
    def test_kakao_login_fail(self):
        client   = Client()
        header   = {'No_Authorizaeion' : '1234'}
        response = client.post('/user/signin', content_type='application/json', **header)
        self.assertEqual(response.status_code, 400)        