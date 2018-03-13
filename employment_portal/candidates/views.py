from django.shortcuts import render
from .models import Candidate
from .admin import CandidateAdmin
from company.models import Employer
from postings.models import Job,JobRequirements

# Create your views here.
def candidates_landing(request):
    uid = request.user.id
    c = Candidate.objects.get(user_id=uid)
    #print(Candidate.objects.all())
    #print(c.objects)
    context = {
        'education': c.education,
        'phone':c.phone_number,
    }
    return render(request, "candidates_landing.html",context)

def candidates_edit_profile(request):

    return render(request,"candidates_edit_profile.html")

def candidate_login(request):
    return render(request,"candidate_login.html")

def candidate_search_companies(request):
    uid = request.user.id
    cand = Candidate.objects.get(user_id=uid)
    company_list=Employer.objects.all()
    context={
        "company_list":company_list
    }
    return render(request,"candidate_search_companies.html",context)

def candidate_search_jobs(request):
    uid=request.user.id
    cand=Candidate.objects.get(user_id=uid)
    job_list=Job.objects.all()
    context={"job_list":job_list}
    return render(request,"candidate_search_jobs.html",context)

def candidate_smart_search(request):
    return render(request,"candidate_smart_search.html")

def candidate_solicit(request):
    uid=request.user.id
    cand=Candidate.objects.get(user_id=uid)
    
    return render(request,"candidate_solicit.html")
