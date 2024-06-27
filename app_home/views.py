from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def chanda_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')  # Replace 'home' with your desired URL name for the home page
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'invalido seu login ou senha.')

    # Render the login form with Bootstrap styles
    return render(request, 'login.html')



def chanda_logout(request):
    logout(request)
    return redirect('home')