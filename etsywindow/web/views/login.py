from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request, user=None):
    if request.method == 'POST':
        # Get the username and password from the POST request
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        # If the user is authenticated, log them in and redirect to the portal page
        if user is not None:
            login(request, user)
            return redirect('portal-home')
        
        # If the user is not authenticated, show an error message
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    
    # If the request method is not POST, show the login page
    else:
        return render(request, 'login.html')
