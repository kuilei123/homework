from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from App01.forms import RegisterForm, LoginForm
from App01.models import User


def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            phone=form.cleaned_data.get('phone')
            user=User(username=username,password=password,email=email,phone=phone)
            print(username,password,email,phone)
            user.save()
            return HttpResponse('首页')
        else:
            return render(request,'register.html',locals())

    return render(request,'register.html')


def verify(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        # 验证
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=User.objects.filter(username=username,password=password).first()
            if user:
                return HttpResponse("验证通过")
            else:
                return HttpResponse('用户不存在')
        else:
            return render(request, 'login.html', locals())

    form = LoginForm()
    return render(request,'login.html',locals())


def send_sms(request):
    from App01.SMS import sms
    from random import randint
    # 判断是ajax请求
    if request.is_ajax():
        # 获取手机号
        phone = request.POST.get('phone')
        # 生成随机验证码
        code = randint(1000, 9999)
        # 把验证码存入session
        request.session['code'] = code
        request.session.set_expiry(20*60)  # 1200秒后失效

        # 拼接模板参数
        param = "{'number':%d}" % code
        # 发送
        res = sms.send(phone, param)
        print(code,phone)
        return JsonResponse({'code':1})
    else :
        # 生成随机验证码
        code = randint(1000,9999)
        # 拼接模板参数
        param = "{'number':%d}" % code
        # 发送
        res = sms.send('17852365173',param)
        print(res)
        print(type(res))
        return HttpResponse("已发送{}".format({code}))


def sms_login(request):
    if request.method == 'POST':
        # 验证短信验证码
        yzm = request.POST.get('yzm')
        # 从session获取存入验证码
        code = str(request.session.get('code'))
        print(code, yzm)
        print(type(code), type(yzm))
        if yzm == code:
            username=request.POST.get('username')
            password=request.POST.get('password')
            phone=request.POST.get('phone')
            user=User.objects.filter(username=username,password=password,phone=phone).first()
            if user:
                return HttpResponse("验证成功")
            else:
                return HttpResponse("用户不存在")

    return render(request,'sms.html')