from django.conf.urls import url
from tdd.app.profile.views import UserProfileView


urlpatterns = [
    url(r'^profile', UserProfileView.as_view(), name='profile'),
    ]
