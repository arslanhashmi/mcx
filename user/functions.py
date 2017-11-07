from .models import *
from datetime import date






#datetimeFormat = '%Y-%m-%d %H:%M:%S'
#current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#print(datetime.strptime(current_time, datetimeFormat) - datetime.strptime(v.creation_time,datetimeFormat))

def get_dict(user):
    return {'name':user.name, 'email': user.email, 'phone':user.phone}


def get_user(email,phone):

    visitor = Visitor.objects.filter(email=email)

    if visitor:
        return True, 'Email already exists'
    visitor = Visitor.objects.filter(phone=phone)
    if visitor:
        return True, 'Phone number already exists'
    return False, "Yo" #return true / false if exists, message wether email exists or phone

def add_user(email,phone,password,name):
    visitor = Visitor(name=name,email=email,phone=phone,password=password,creation_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    visitor.save()

    return get_dict(visitor)

def find_user(email, password='no'):
    try:
        user = Visitor.objects.get(email=email)
    except:
        return False, 'Email does not exists.'

    if password != 'no':
        if user:
            if password!= user.password:
                return False, 'Password is incorrect.'
            else:
                return True, get_dict(user)
    dict = get_dict(user)
    dict['password'] = user.password
    return True, dict

def check_token(email):

    try:
        visitor = Visitor.objects.get(email=email)
        datetimeFormat = '%Y-%m-%d %H:%M:%S'
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_left = datetime.strptime(current_time, datetimeFormat) - datetime.strptime(visitor.creation_time,datetimeFormat)
        if ',' in str(time_left):
            return int(str(time_left).split(',')[0].split(' ')[0]) < int(visitor.days)
            #return int(str(time_left)[0])
        #else:
        #    return int(str(time_left)[-4]) or int(str(time_left)[-7])
        else:
            return 0
    except:
        return 0

def find_url(exchange,symbol,request):
    exists = check_url(exchange,symbol,request)
    if exists:
        return True, ""
    else:
        try:
            image = Image.objects.get(exchange=exchange, symbol=symbol)
            return False, (image.image_path)
        except:
            return True, ''

def check_url(exchange,symbol,request):
    try:
        if [exchange,symbol] in request.session['urls']:
            #print(request.session['urls'])
            return True
        else:
            #print(request.session['urls'])
            request.session['urls'].append([exchange,symbol])
            request.session.modified = True
            return False
    except:
        request.session['urls'].append([exchange, symbol])
        request.session.modified = True
        return False