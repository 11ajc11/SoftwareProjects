from django.shortcuts import render
from .models import Recruiter
from company.models import Employer
def recruiters_landing(request):
    uid = request.user.id
    recruiter=Recruiter.objects.get(user_id=uid)
    employer=Employer.objects.get(user_id=recruiter.Employer_Name.user_id)
    context={'recruiter':recruiter, 'CompanyName':employer.name_english}
    return render(request,"recruiters_landing.html",context)

def recruiters_postings(request):
    return render(request,"recruiters_postings.html")
def recruiters_sent_offers(request):
    return render(request,"recruiters_sent_offers.html")
def recruiters_smart_match(request):
    return render(request,"recruiters_smart_match.html")
def recruiters_view_post(request):
    return render(request,"recruiters_view_post.html")
def recruiters_view_solicitations(request):
    return render(request,"recruiters_view_solicitations.html")
