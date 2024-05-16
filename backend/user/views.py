from django.contrib.auth import authenticate, login, logout
from user.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages

# View for home page
def home(request):
    if request.user.is_authenticated:
        return render(request, 'user/home.html')
    else:
        messages.error(request, 'You must be a site admin to access this page!')
        return redirect('login')

# View for login page
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user =  authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {user.first_name} {user.last_name}!')
                return redirect('home')
            else:
                messages.error(request, 'Incorrect username or password, please try again!')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

# View for logout page

# View for edit info page

# View for change password page
