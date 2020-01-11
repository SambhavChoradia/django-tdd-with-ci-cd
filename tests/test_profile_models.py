from rest_framework.test import APITestCase
from tdd.app.user.models import User
from tdd.app.profile.models import UserProfile

class UserModelTestCase(APITestCase):

    def test_create_profile_model(self):
        user = User.objects.create_user(
            email='ram@gmail.com',
            password='123456'
            )
        UserProfile.objects.create(
            user=user,
            first_name='ram',
            last_name='kumar',
            phone_number='1234567890',
            age=10
            )
        assert UserProfile.objects.count() == 1, 'Should be equal'
