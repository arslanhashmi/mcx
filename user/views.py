from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.shortcuts import render, reverse, redirect
import json
import re
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from mcx.settings import EMAIL_HOST_USER
from .functions import *


class Index(View):
    def get(self,request):
        try:
            if request.session['user']:
                return redirect(reverse('profile'))
        except:
            return render(request, 'index-2.html')

    def post(self,request):
        if request.POST.get('form-type') == 'register-form':
            email = str(request.POST.get('email')).lower()
            phone = str(request.POST.get('phone'))
            name = str(request.POST.get('full-name')).lower()
            password = str(request.POST.get('password'))

            if len(name)<1:
                return HttpResponse(json.dumps({'message': "Full name is required"}), content_type="application/json")
            if len(email)<1:
                return HttpResponse(json.dumps({'message': "Email is required"}), content_type="application/json")
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
            if match is None:
                return HttpResponse(json.dumps({'message': "Please enter a valid email"}), content_type="application/json")
            if not str(phone).isdigit():
                    return HttpResponse(json.dumps({'message': 'Phone number should be numeric '}), content_type='application/json')
            if len(phone)<10:
                return HttpResponse(json.dumps({'message': "Phone number is not correct"}), content_type="application/json")
            exists, message = get_user(email, phone)
            if exists:
                return HttpResponse(json.dumps({'message': message}),
                                    content_type="application/json")

            if len(password) > 16 or len(password) < 6:
                return HttpResponse(json.dumps({'message': 'The password length should be atleast than 6'}), content_type='application'
                                                                                                         '/json')

            user = add_user(email=email,name=name,password=password,phone=phone)
            request.session['user'] = user
            return HttpResponse(json.dumps({'message': 'Added'}), content_type="application/json")

        elif request.POST.get('form-type') == 'login-form':
            email = str(request.POST.get('email')).lower()
            password = str(request.POST.get('password'))
            exists, user = find_user(email, password)
            if not exists:
                return HttpResponse(json.dumps({'message': user}),
                                    content_type='application'
                                                 '/json')
            else:
                request.session['user'] = user
                return HttpResponse(json.dumps({'message': 'exists'}),
                                    content_type='application'
                                                 '/json')

        elif request.POST.get('form-type') == 'forget-form':
            email = str(request.POST.get('email')).lower()
            exists, user = find_user(email)
            if not exists:
                return HttpResponse(json.dumps({'message': 'Email is not registered'}),
                                    content_type='application'
                                                 '/json')
            else:
                try:
                    message = 'You can login by using your old password:'+user['password']

                    #send_mail('RESET PASSWORD ( trustedavatar.com )', "this is a message", EMAIL_HOST_USER,
                              #user['email'])
                    return HttpResponse(json.dumps({'message': 'Check your email for password!'}),
                                        content_type='application'
                                                     '/json')
                except:
                    return HttpResponse(json.dumps({'message': 'Some problem occurred!'}),
                                    content_type='application'
                                                 '/json')
        else:
            return HttpResponse(json.dumps({'message': 'Something went wrong.'}), content_type="application/json")


class ImagePage(View):
    def get(self,request):
        try:
            if request.session['user']:
                if check_token(request.session['user']['email']):
                    request.session['urls']=[]
                    return render(request, 'image-page.html',{
                        'username':request.session['user']['name'],
                        'token': 1,
                        'images':[]
                    })
                else:
                    return render(request, 'image-page.html',{
                        'username':request.session['user']['name'],
                        'token': 0
                    })

        except:
            return redirect(reverse('index'))

    def post(self,request):
        print('in post')
        exchange = str(request.POST.get('exchange'))
        symbol = str(request.POST.get('symbol'))
        type = str(request.POST.get('type'))
        print(exchange,symbol,type)
        if type == 'push':
            if exchange == 'nothing':
                return HttpResponse(json.dumps({'message': 'nothing'}), content_type="application/json")
            alreadyExistsOrProblem, url = find_url(exchange,symbol,request)
            if alreadyExistsOrProblem:
                return HttpResponse(json.dumps({'message': 'exists'}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'message': url}), content_type="application/json")
        else:
            try:
                request.session['urls'].remove([exchange,symbol])
                request.session.modified = True
                return HttpResponse(json.dumps({'message': 'poped'}), content_type="application/json")
            except:
                return HttpResponse(json.dumps({'message': 'Some error occured'}), content_type="application/json")


class Logout(View):
    def get(self, request):
        try:
            request.session.clear()
        except:
            pass
        return redirect(reverse('index'))







