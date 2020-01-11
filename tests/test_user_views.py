import json
from rest_framework.test import APITestCase
from django.urls import reverse
from tdd.app.user.models import User

class UserLoginTestCase(APITestCase):
    url = reverse('signin')

    def setUp(self):
        self.email = 'ram@gmail.com'
        self.password = '123456'
        self.user = User.objects.create_user(self.email, self.password)

    def test_authentication_without_password(self):
        response = self.client.post(self.url, {'email': 'ram@gmail.com'})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_wrong_password(self):
        response = self.client.post(self.url, {'email': self.email, 'password': 'I_know'})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_valid_data(self):
        response = self.client.post(self.url, {'email': self.email, 'password': self.password})
        self.assertEqual(200, response.status_code)
        self.assertTrue('token' in json.loads(response.content))
        self.assertEqual(response.data, {
            'success': 'True',
            'status code': 200,
            'message': 'User logged in  successfully',
            'token': response.data['token']
            })


class UserRegistrationTestCase(APITestCase):
    url = reverse('signup')

    def test_user_registration_with_valid_data(self):
        user = {
            'email':'ram@gmail.com',
            'password':'123456',
            'profile': {
                'first_name': 'ram',
                'last_name': 'kumar',
                'phone_number': '1234567891',
                'age': 11,
                'gender': 'M'
                }
            }
        response = self.client.post(self.url, user)
        self.assertTrue(201, response.status_code)
        self.assertEqual(response.data, {'success': 'True', 'status code': 200, 'message': 'User registered  successfully'})

    def test_unique_user_registration(self):
        user = {
            'email':'ram@gmail.com',
            'password':'123456',
            'profile': {
                'first_name': 'ram',
                'last_name': 'kumar',
                'phone_number': '1234567891',
                'age': 11,
                'gender': 'M'
                }
            }
        response = self.client.post(self.url, user)
        self.assertTrue(201, response.status_code)
        self.assertEqual(response.data, {'success': 'True', 'status code': 200, 'message': 'User registered  successfully'})

        user = {
            'email':'ram@gmail.com',
            'password':'123456',
            'profile': {
                'first_name': 'ram',
                'last_name': 'kumar',
                'phone_number': '1234567891',
                'age': 11,
                'gender': 'M'
                }
            }

        response = self.client.post(self.url, user)
        self.assertTrue(400, response.status_code)
