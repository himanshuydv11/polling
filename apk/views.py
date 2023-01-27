from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import Question
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def location(request):
    return render(request, 'location.html')


def usersignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password']
        if len(username) > 10:
            messages.error(request, 'usename must be under 10 characters')
            return redirect('signup')

        if User.objects.filter(username = username):
            messages.error(request, 'Username already exists Please try some other username')
            return redirect('signup')
        
        if User.objects.filter(email = email):
            messages.error(request, 'Email already registered')
            return redirect('signup')

        if not username.isalnum() :
            return redirect('home')

        if not username.islower() :
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.save()
        messages.success(request, 'Your account created successfully')
        return redirect('login')
        
    else:
        return render(request, 'usersignup.html')

def usersign(request):
    return render(request, 'usersign.html')



def loginhere(request):
    if request.method == 'POST':
        loginusername = request.POST['loginuser']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged In')
            return redirect('profile')
        
        else:
            messages.error(request, 'Bad Credentials')
            return redirect('signup')
    else:
        return render(request, 'userloginpage.html')


def logouthere(request):
    logout(request)
    messages.success(request, 'Logged out Successfully')
    return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        ques = Question.objects.all()
        args = {'user' : request.user, 'ques' : ques}
        return render(request, 'profile.html', args)
    else:
        return redirect('login')

def create_poll(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            question = request.POST['question']
            ans = request.POST['answer']
            op1 = request.POST['op1']
            op2 = request.POST['op2']
            op3 = request.POST['op3']
            op4 = request.POST['op4']
            poll = Question(question=question, answer=ans, op1=op1, op2=op2, op3=op3, op4=op4)
            poll.save()
            messages.success(request, 'Question created successfully')
            return redirect('profile')
        else:
            return render(request, 'createpoll.html')
    else:
        return render(request, 'userloginpage.html')
    