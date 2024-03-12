from django.shortcuts import render

# Create your views here.






from django.shortcuts import render

from django.shortcuts import render , HttpResponse ,redirect
from django.contrib.auth.models import User


from django.contrib.auth import authenticate , login , logout
from .models import room_rent , room_money

import razorpay

from django.views.decorators.csrf import csrf_exempt

RAZORPAY_API_KEY = 'rzp_test_QFDGWUnkj7cVhJ'
RAZORPAY_API_SECRET_KEY = 'rQSNHhtGd0r0u8GAkNqjlnTm'

client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))

from django.db.models import Q

def home(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        # Filter room_rent objects based on room_location containing the search query
        # Use Q object to filter results based on city, country, and dist
        objs = room_rent.objects.filter(
            Q(room_location__icontains=search_query) |
            Q(location_city__icontains=search_query) |
            Q(location_country__icontains=search_query) |
            Q(location_state__icontains=search_query) |
            Q(location_dist__icontains=search_query)
        )
    else:
        # If no search query is provided, display all room_rent objects
        objs = room_rent.objects.all()

    return render(request, 'home.html', {'datas': objs})


def detail_page(request,id):
    if request.method == 'POST':
        user = request.user
        obj_user = room_rent.objects.get(id=id)
        name = request.user.username
        amount = obj_user.room_prize
        currencyx = "INR"

        print(user , obj_user , name , amount , currencyx)

        payment_order = client.order.create(dict(amount = amount , currency = currencyx,payment_capture=1))
        payment_order_id = payment_order['id']


        context = {
        'amount':amount , 'api_key':RAZORPAY_API_KEY ,'order_id':payment_order_id ,'name':name
    }

        
        return render(request , 'detail.html',context)

    

 

        
    objs  = room_rent.objects.filter(id=id).first()

    return render(request ,'detail.html',{'obj':objs})





def register_page(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        passx = request.POST.get('passx')

        print(fname, lname, email,passx ,username )



        obj = User.objects.create(username = username , first_name=fname,last_name=lname,email=email )
        obj.set_password(passx)
        obj.save()

        print(fname, lname, email,passx ,username )

    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        passx = request.POST['passx']

        if User.objects.filter(username=username).exists():
            user_obj = authenticate(username=username,password=passx)
            login(request,user_obj)
            print('login sucess using ...')
            print(username,passx)
            return redirect('/')

        else:
            return HttpResponse('any error occuredin if statement')

    return render(request , 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/')