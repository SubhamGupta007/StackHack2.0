from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegisterForm, ProfileRegisterForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.forms import modelformset_factory
from django.db import IntegrityError, transaction
from django.contrib import messages

def home(request):
    return(render(request, "client/home.html", {}))

def LoginPage(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('client:home'))
        else:
            print("Error")
    return(render(request, "client/login.html", context))

def SignUpPage(request):
    if request.method  == 'POST':
        form = UserRegisterForm(request.POST or None)
        p_reg_form = ProfileRegisterForm(request.POST,request.FILES or None)
        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()
            p_reg_form_instance = p_reg_form.save(commit=False)
            p_reg_form_instance.user = user
            p_reg_form_instance.save()

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            login(request, user)
            return redirect(reverse_lazy('client:home'))
        else:
            form = UserRegisterForm(request.POST,request.FILES or None)
            p_reg_form = ProfileRegisterForm(request.POST,request.FILES or None)
            context = {
                'form': form,
                'p_reg_form': p_reg_form,
            }
    else:
        form = UserRegisterForm()
        p_reg_form = ProfileRegisterForm()
        context = {
                'form': form,
                'p_reg_form': p_reg_form,
            }
    return render(request, 'client/register.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse_lazy('client:home'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'client/password_change.html', {
        'form': form
    })
