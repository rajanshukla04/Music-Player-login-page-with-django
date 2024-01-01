from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from Members.models import UserProfile
from .forms import SignupForm
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def your_django_signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        mobile = request.POST['mobile']
        address = request.POST['address']
        password = request.POST['password']

       # Check if a user with the given email or mobile number already exists
        if UserProfile.objects.filter(email=email).exists() or UserProfile.objects.filter(mobile=mobile).exists():
            # Set an error message if the email or mobile number is already in use
            error_message = 'User with this email or mobile number already registered. Try a different email or mobile number.'
        else:
            # Create a new UserProfile object and save it to the database
            user_profile = UserProfile.objects.create(
                name=name,
                email=email,
                mobile=mobile,
                address=address,
                password=password
            )
         # Redirect to the login page
            return HttpResponseRedirect('login')  # Replace 'login' with the URL of your login page

    return render(request, 'signup.html', {'error_message': error_message})


def your_login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if a user with the given email or mobile number already exists
        if UserProfile.objects.filter(email=username).exists() or UserProfile.objects.filter(mobile=username).exists():
            # User exists, proceed with authentication logic
            # ...
            # Redirect to the home page
            return HttpResponseRedirect('/')  
        else:
            # User does not exist, set an error message
            error_message = 'Invalid login credentials. Please try again.'
        return render(request, 'login.html', {'error_message': error_message})