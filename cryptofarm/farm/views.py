from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError

from .models import User, Wallet

# Create your views here.
def index(request):
    return render(request, "farm/index.html")

def start(request):
    return render(request, "farm/start.html")

def login_view(request):
    # If user is submitting the login form:
    if request.method == "POST":
        # Get username and password from the form:
        username = request.POST["username"]
        password = request.POST["password"]
        # Try to authenticate the user:
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'),)
        else:
            return render(request, 'farm/login.html', {
                "message": "Invalid username and/or password"
            })
    # If user is calling the login page:
    else:
        return render(request, "farm/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            return render(request, "farm/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "farm/register.html")
