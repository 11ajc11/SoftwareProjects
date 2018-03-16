from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserSignUp, LoginForm
from .models import UserProfile
from candidates.models import Candidate
from company.models import Employer

def candidatesignup(request):
    if request.method=='POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            p = UserProfile()
            p.user_type='candidate'
            p.user = user
            p.save()
            cand = Candidate()
            cand.user = user
            cand.education = 'Depaul'
            cand.date_of_birth = '1223-3-2'
            cand.save()
            login(request, user)
            return redirect('candidates:candidates_edit_profile')
    else:
        form = UserSignUp()
    return render(request, 'candidate_signup.html', {'form': form})

def companysignup(request):
    if request.method=='POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_type = 'Company'
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            p = UserProfile()
            p.user_type = 'company'
            p.user = user
            p.save()
            comp = Employer()
            comp.user = user
            comp.website = 'www.thissitesucks.com'
            comp.bio = 'Im just a regular guy'
            comp.save()
            login(request, user)
            return redirect("company:cadmin_edit_profile")
    else:
        form = UserSignUp()
    return render(request, 'cadmin_signup.html', {'form': form})

def candidatelogin(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect("candidates:candidates_landing")
    return render(request, 'candidate_login.html', {'form': form})

def companylogin(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect("company:cadmin_landing")# Redirect to a success page.
    return render(request, 'cadmin_login.html', {'form': form})
