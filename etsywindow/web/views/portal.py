from django.shortcuts import render, redirect


def portal_home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    print(request.user.id)
    return render(request, 'portal_home.html')
    