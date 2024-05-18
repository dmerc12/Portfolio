from user.forms import LoginForm, EditUserForm, ChangePasswordForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

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
                return redirect('contact-home')
            else:
                messages.error(request, 'Incorrect username or password, please try again!')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

# View for logout functionality
def logout_user(request):
    logout(request)
    messages.success(request, 'Goodbye!')
    return redirect('login')

# View for edit user page
def edit_user(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.pk)
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                login(request, user)
                messages.success(request, 'Information successfully edited!')
                return redirect('contact-home')
        else:
            form = EditUserForm(instance=user)
        return render(request, 'user/edit.html', {'form': form})
    else:
        messages.error(request, 'You must be a site admin to access this page!')
        return redirect('login')

# View for change password page
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangePasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                login(request, request.user)
                messages.success(request, 'Password successfully changed!')
                return redirect('contact-home')
        else:
            form = ChangePasswordForm(request.user)
        return render(request, 'user/change-password.html', {'form': form})
    else:
        messages.error(request, 'You must be a site admin to access this page!')
        return redirect('login')
