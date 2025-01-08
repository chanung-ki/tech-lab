from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User
from django.urls import reverse

class UserAPITest(APITestCase):
    def test_get_user(self):
        """
            유저 정보를 조회할 수 있어야 한다.
        """
        
        # test 객체 생성
        user_instance = User.objects.create(
            email='test@test.com',
            name='test_user'
        )
        
        url = reverse('get_user_detail', kwargs={'id': user_instance.id})
        
        # API 호출
        response = self.client.get(url)
        
        # response status code 확인
        self.assertEqual(response.status_code, status.HTTP_200_OK, '200 code가 아니다.')
        
        # response 데이터에서 email 값 확인
        self.assertEqual(response.data['email'], 'test@test.com', '이메일이 일치하지 않는다.')
        
        # response 데이터에서 name 값 확인
        self.assertEqual(response.data['name'], 'test_user', '이름이 일치하지 않는다.')
        
        # created_at 값이 None이 아니어야 한다
        self.assertIsNotNone(response.data['created_at'], '가입날짜가 None이다.')
        
        
        