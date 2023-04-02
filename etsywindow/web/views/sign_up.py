from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import User


def sign_up(request):
    if request.method == 'POST':
    # create a User instance with the validated form data
        user = User(
            first_name=request.POST['first-name'],
            last_name=request.POST['last-name'],
            email_address=request.POST['email'],
        )
        print("\n### HERE ###")
        print("email:", user.first_name)
        print("email:", user.last_name)
        print("email:", user.email_address)
        if not user.email_address:
            # TODO: Force email required on form
            messages.error(request, "Email is required")
            context = {
                'first_name': request.POST.get('first-name', ''),
                'last_name': request.POST.get('last-name', ''),
                'email_address': '',
            }
            return render(request, 'sign_up.html', context=context)

        # set and validate the password
        password = request.POST['password']
        password_verify = request.POST['password-verify']

        if password != password_verify:
            # TODO: Force password required on form
            # TODO: Add a toast pop up for the user
            messages.error(request, "Passwords do not match")
            # TODO: Redirect but keep form populated
            return redirect('sign-up')

        # TODO: Need to figure out this password stuff
        #user.password(password)

        # save the user to the database
        user.save()

        messages.success(request, "Your account has been created!")

        return redirect('home') # TODO Need to get this to a different portal page
    else:
        # TODO: If all goes well then redirect to the portal as a logged in user
        #return redirect('home') # TODO Need to get this to a different portal page
        return render(request, 'sign_up.html')