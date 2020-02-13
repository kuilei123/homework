

from django.urls import path

from App01 import views
app_name='App01'
urlpatterns = [
    path('register/',views.register,name='register'),
    # 第三方验证码
    path('verify/', views.verify, name='verify'),
    # 发送短信验证码
    path('sms/',views.send_sms,name='sms'),

    # 短信登录
    path('smslogin/',views.sms_login,name='smslogin'),
]
