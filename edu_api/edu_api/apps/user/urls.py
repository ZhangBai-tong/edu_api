from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token

from user import views

urlpatterns = [
    path("login/", obtain_jwt_token),
    path("sign_in/", views.UserAPIView.as_view()),
    path("message/", views.SendMessageAPIView.as_view()),
    path("captcha/", views.CaptchaAPIView.as_view()),
    path("check_phone/", views.CheckPhoneNumber.as_view({'post': 'check_phone'})),
    path("login_message/", views.MessageModel.as_view({'post': 'login_message'})),
]
