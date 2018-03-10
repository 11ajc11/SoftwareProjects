from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from user_accounts.forms import UserSignUp, LoginForm

def candidatesignup(request):
    if request.method=='POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('candidate_login_success.html')
    else:
        form = UserSignUp()
    return render(request, 'candidate_signup.html', {'form': form})

def companysignup(request):
    if request.method=='POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('cadmin_edit_profile.html')
    else:
        form = UserSignUp()
    return render(request, 'cadmin_signup.html', {'form': form})

def candidatelogin(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect("candidate_login_success.html")
    return render(request, 'candidate_login.html', {'form': form})

def companylogin(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect("cadmin_landing.html")# Redirect to a success page.
    return render(request, 'cadmin_login.html', {'form': form})




