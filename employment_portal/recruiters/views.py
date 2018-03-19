from django.shortcuts import render
from .models import Recruiter
from company.models import Employer
from recruiters.models import Recruiter
from postings.models import Job
from offer_solicit.models import Solicitation
from candidates.models import Candidate
from offer_solicit.models import Offer_Invitation
from datetime import datetime
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

def recruiters_smart_match(request,job_id):
    uid = request.user.id
    recruiter=Recruiter.objects.get(user_id=uid)
    job = Job.objects.get(id = job_id)
    candlist = Candidate.objects.all()
    scorelist = []
    for cand in candlist:
        rating = 0
        if cand.skills_choices_1 == job.job_skills_1 or job.job_skills_2:
            rating += 10
        if cand.skills_choices_2 == job.job_skills_2 or job.job_skills_3:
            rating += 9
        if cand.skills_choices_3 == job.job_skills_3 or job.job_skills_4:
            rating += 8
        if cand.skills_choices_4 == job.job_skills_4 or job.job_skills_5:
            rating += 7
        if cand.skills_choices_5 == job.job_skills_5:
            rating += 6
        if cand.skills_choices_6 == job.job_skills_6:
            rating += 5
        if cand.skills_choices_7 == job.job_skills_7:
            rating += 4
        if cand.skills_choices_8 == job.job_skills_8:
            rating += 3
        if cand.skills_choices_9 == job.job_skills_9:
            rating += 2
        if cand.skills_choices_10 == job.job_skills_10:
            rating += 1

        if rating >= 20:
           scorelist.append((rating,cand))
    scorelist=sorted(scorelist, key=lambda temp: temp[0], reverse=True)
    context={'scorelist':scorelist, 'job_id':job_id}
    return render(request,"recruiters_smart_match.html",context)



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
        new.candidate = Candidate.objects.get(user_id=cand_id)
        new.job = Job.objects.get(pk=job_id)
        new.created = datetime.now()
        new.save()
        uid = request.user.id
        recruiter=Recruiter.objects.get(user_id=uid)
        employer=Employer.objects.get(user_id=recruiter.Employer_Name.user_id)
        context={'recruiter':recruiter, 'CompanyName':employer.name_english}
        return render(request,"recruiters_landing.html",context)
    else:
        cand=Candidate.objects.get(user_id=cand_id)
        job=Job.objects.get(id=job_id)
        context={'cand':cand, 'job':job}
        return render(request, 'recruiters_cand_detail.html',context)
