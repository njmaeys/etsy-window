from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import User


def get_started(request):
    if request.method == 'POST':
    # create a User instance with the validated form data
        user = User(
            first_name=request.POST['first-name'],
            last_name=request.POST['last-name'],
            email_address=request.POST['email'],
        )

        # set and validate the password
        password = request.POST['password']
        password_verify = request.POST['password-verify']

        if password != password_verify:
            # TODO: Add a toast pop up for the user
            messages.error(request, "Passwords do not match")
            # TODO: Redirect but keep form populated
            return redirect('get-started')

        # TODO: Need to figure out this password stuff
        #user.password(password)

        # save the user to the database
        user.save()

        messages.success(request, "Your account has been created!")

        return redirect('home') # TODO Need to get this to a different portal page
    else:
        # TODO: If all goes well then redirect to the portal as a logged in user
        return render(request, 'get_started.html')