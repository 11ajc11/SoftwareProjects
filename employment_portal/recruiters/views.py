from django.shortcuts import render
from .models import Recruiter
from company.models import Employer
from recruiters.models import Recruiter
from postings.models import Job
from offer_solicit.models import Solicitation
def recruiters_landing(request):
    uid = request.user.id
    recruiter=Recruiter.objects.get(user_id=uid)
    employer=Employer.objects.get(user_id=recruiter.Employer_Name.user_id)
    context={'recruiter':recruiter, 'CompanyName':employer.name_english}
    return render(request,"recruiters_landing.html",context)

def recruiters_postings(request):
    uid = request.user.id
    recruiter=Recruiter.objects.get(user_id=uid)
    job_list=Job.objects.filter(recruiter=recruiter)
    context={'job_list': job_list}
    return render(request, "recruiters_postings.html", context)

def recruiters_sent_offers(request):
    return render(request,"recruiters_sent_offers.html")

def recruiters_smart_match(request):
    return render(request,"recruiters_smart_match.html")
def recruiters_view_post(request):
    return render(request,"recruiters_view_post.html")
def recruiters_view_solicitations(request):
    uid = request.user.id
    recruiter=Recruiter.objects.get(user_id=uid)
    solicitation_list=Solicitation.objects.filter(job__recruiter=recruiter)
    context={'solicitation_list':solicitation_list}
    return render(request,"recruiters_view_solicitations.html",context)
    
def recruiter_cand_detail(request, cand_id, job_id):

    if request.method == 'POST':
        uid = request.user.id
        new = Offer_Invitation()
        new.candidate = Candidate.objects.get(user_id=uid)
        new.job = Job.objects.get(pk=job_id)
        new.created = datetime.now()
        new.save()
        job_list = Job.objects.all()
        context = {"job_list": job_list}
        return render(request, "recruiters_smart_match.html", context)
    else:
        return render(request, 'recruiters_landing.html')
