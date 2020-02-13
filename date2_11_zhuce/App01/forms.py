

#注册表单
import re

from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from App01.models import User
def check_password(Value):
    if re.match(r'\d*$',Value):
        raise ValidationError('密码不能是纯数字')

class RegisterForm(forms.Form):
    username=forms.CharField(label='用户名',min_length=6,required=True,
                             error_messages={'required':'用户名不能为空','min_length':'用户名长度必须大于6位'})
    password=forms.CharField(label='密码',min_length=6,max_length=12,
                             required=True,
                             # validators=[RegexValidator(regex=r'\d*$', message="密码不能是纯数字",code='password')],
                             validators=[check_password],
                             error_messages={'min_length':'密码长度必须大于6，小于12','max_length':'密码长度必须大于6，小于12','required':'密码不能为空'})
    confirm_password = forms.CharField(label='确认密码', min_length=6, max_length=12,
                               required=True,
                               validators=[check_password],
                               error_messages={'min_length': '密码长度必须大于6，小于12', 'max_length': '密码长度必须大于6，小于12',
                                               'required': '密码不能为空'})
    email = forms.EmailField(error_messages={'invalid':'邮箱格式不正确'})
    phone=forms.CharField(label='手机号',min_length=11,max_length=11,
                          required=True,
                          validators=[RegexValidator(regex=r"^1[35678]\d{9}$",message='手机号格式不对',code='phone')],
                          error_messages={'min_length':'手机号必须11位','max_length':'手机号必须11位',
                                          'required':'手机号不能为空'})

    def clean_username(self):
        # 获取用户名
        username = self.cleaned_data.get('username')
        # 查询数据库
        # 如果存在
        if User.objects.filter(username=username).first():
            raise ValidationError("用户名重复")
        # 必须把正确数据返回
        return username

    def clean_phone(self):
        # 获取用户名
        phone = self.cleaned_data.get('phone')
        # 查询数据库
        # 如果存在
        if User.objects.filter(phone=phone).first():
            raise ValidationError("手机号已存在")
        # 必须把正确数据返回
        return phone
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).first():
            raise ValidationError('邮箱已存在')
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        # 判断两者是否相等
        if password != confirm_password:
            raise ValidationError({'confirm_password':["两次密码输入不一致"]})
        return self.cleaned_data


# 登录
class LoginForm(forms.Form):
    username = forms.CharField(required=True,error_messages={
        'required':'用户名必须输入'
    })
    password = forms.CharField()
    captcha = CaptchaField()  # 验证码字段

# class SMSlogin(forms.Form):
#     username = forms.CharField(required=True, error_messages={
#         'required': '用户名必须输入'
#     })
#     password = forms.CharField()
#     phone = forms.CharField()
#


