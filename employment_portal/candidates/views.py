from django.shortcuts import render
from .models import Candidate
from .admin import CandidateAdmin
from company.models import Employer
from postings.models import Job,JobRequirements
from offer_solicit.models import Solicitation,Offer_Invitation
from candidates.forms import CandidateForm
from django.views.generic.edit import FormView
from .admin import CandidateAdmin

# Create your views here.
class candidateeditprofileview(FormView):
    template_name = 'candidates_edit_profile.html'
    form_class = CandidateForm
    success_url = 'success.html'
# Create your views here.
def candidates_landing(request):
    uid = request.user.id
    user = Candidate.objects.get(user_id=uid)
    context = {
        'username':user.user,
        'nearest_metropolitan_city':user.nearest_metropolitan_city,
        'education': user.education_university,
        'bio':user.bio,
        "skills_choice_1":user.skills_choices_1,
        "skills_choice_2":user.skills_choices_2,
        "skills_choice_3":user.skills_choices_3,
        "skills_choice_4":user.skills_choices_4,
        "skills_choice_5":user.skills_choices_5,
        "skills_choice_6":user.skills_choices_6,
        "skills_choice_7":user.skills_choices_7,
        "skills_choice_8":user.skills_choices_8,
        "skills_choice_9":user.skills_choices_9,
        "skills_choice_10":user.skills_choices_10,
    }
    return render(request, "candidates_landing.html",context)



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
    solicitation_list=Solicitation.objects.filter(candidate__user_id=uid)
    context={"solicitation_list":solicitation_list}
    return render(request,"candidate_solicit.html",context)
def candidate_offers(request):
    uid=request.user.id
    cand=Candidate.objects.get(user_id=uid)
    offer_list=Offer_Invitation.objects.filter(candidate__user_id=uid)
    context={"offer_list":offer_list}
    return render(request,"candidate_offers.html",context)
