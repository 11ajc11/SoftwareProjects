from django.shortcuts import render
from .models import Candidate
from .admin import CandidateAdmin

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
    return render(request,"candidate_search_companies.html")

def candidate_search_jobs(request):
    return render(request,"candidate_search_jobs.html")

def candidate_smart_search(request):
    return render(request,"candidate_smart_search.html")

def candidate_solicit(request):
    return render(request,"candidate_solicit.html")
