from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def sign_up(request):
    if request.method == 'POST':
        # create a User instance with the validated form data
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']

        if not email:
            messages.error(request, "Email is required")
            return redirect('sign-up')

        # check if a user with the given email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "A user with that email already exists")
            return redirect('sign-up')

        # hash the password and create the user
        hashed_password = make_password(password)
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=email,
            email=email,
            password=hashed_password,
        )
        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'sign_up.html')