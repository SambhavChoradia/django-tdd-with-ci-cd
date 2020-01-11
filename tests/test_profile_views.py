import json
from rest_framework.test import APITestCase #, APIClient
from django.urls import reverse
from tdd.app.user.models import User
from tdd.app.profile.models import UserProfile


class UserProfileTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(
            email='ram@gmail.com',
            password='123456'
            )
        UserProfile.objects.create(
            user=user,
            first_name='ram',
            last_name='kumar',
            phone_number='1234567890',
            age=10,
            gender='M'
            )

    def test_fetch_user_detail_with_valid_token(self):
        url = reverse('signin')
        response = self.client.post(url, {'email': 'ram@gmail.com', 'password': '123456'})
        self.assertEqual(200, response.status_code)
        self.assertTrue('token' in json.loads(response.content))
        token = response.data['token']

        url = reverse('profile')
        # client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.data, {
            'success': 'true',
            'status code': 200,
            'message': 'User profile fetched successfully',
            'data': {
                'first_name': 'ram',
                'last_name': 'kumar',
                'phone_number': '1234567890',
                'age': 10,
                'gender':'M'
            }

        })

    def test_fetch_user_detail_with_invalid_token(self):
        url = reverse('signin')
        response = self.client.post(url, {'email': 'ram@gmail.com', 'password': '123456'})
        self.assertEqual(200, response.status_code)
        self.assertTrue('token' in json.loads(response.content))
        token = response.data['token']

        url = reverse('profile')
        # client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token+'i'))
        response = self.client.get(url)
        self.assertEqual(401, response.status_code)
