from django.conf.urls import url
from tdd.app.user.views import UserRegistrationView
from tdd.app.user.views import UserLoginView

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view(), name='signup'),
    url(r'^signin', UserLoginView.as_view(), name='signin'),
    ]
