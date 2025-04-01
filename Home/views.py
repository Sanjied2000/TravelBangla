from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Package,Booking



from django.http import HttpResponse,request
@login_required
def index(request):
    return render(request,'index.html')


def packages(request):
    packages = Package.objects.all()
    return render(request,'packages.html',{'packages': packages})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Log the user in
            messages.success(request, 'Login successful!')
            return redirect('index')  # Redirect to the homepage or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')  

    return render(request, 'login.html') 

def user_reg(request):
    if request.method =='POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')

    return render(request,'register.html')          
    
def user_logout(request):
    auth_logout(request)

    return redirect('index')        
    
def aboutus(request):
    return render(request,'aboutus.html')

def dashboard(request,id):
    user_obj= User.objects.get(id=id)
    dashitems= Booking.objects.filter(user=user_obj)
    return render(request,'dashboard.html',{'dashitems':dashitems})

def details(request,pName):
    
    package = Package.objects.get(pName=pName)
    return render(request,'package_details.html',{'package':package})

def booking(request,pName):
    if request.method == 'POST':
        id= request.user.id
        user_obj= User.objects.get(id=id)            
        package = Package.objects.get(pName=pName)

        

        numberofpeople = int(request.POST.get("num_people",1))
        date = request.POST.get('travel_date')
        book=Booking.objects.create(package=package,user=user_obj,date=date,numberofpeople=numberofpeople,status="UnPaid")
        book.save()

        return redirect('dashboard', id=request.user.id)
    id= request.user.id
    user_obj= User.objects.get(id=id)        
    
    package = Package.objects.get(pName=pName)
    return render(request,'booking.html',{'package':package,'user':user_obj})

def cancel(request,id):
    book=Booking.objects.get(id=id)
    book.delete()
   

    return redirect('dashboard', id=request.user.id)