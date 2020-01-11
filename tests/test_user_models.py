from rest_framework.test import APITestCase
from tdd.app.user.models import User

class UserModelTestCase(APITestCase):

    def test_create_user_model(self):
        User.objects.create_user(email='ram@gmail.com', password='123456')
        assert User.objects.count() == 1, 'Should be equal'
