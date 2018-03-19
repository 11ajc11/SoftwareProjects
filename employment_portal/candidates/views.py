from django.shortcuts import render, get_object_or_404
from candidates.models import Candidate
from .admin import CandidateAdmin
from company.models import Employer
from postings.models import Job,JobRequirements
from offer_solicit.models import Solicitation,Offer_Invitation
from candidates.forms import CandidateForm
from django.views.generic.edit import FormView
from .admin import CandidateAdmin
from datetime import datetime

# Create your views here.
def candidateeditprofileview(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data.get('bio')
            education_university = form.cleaned_data.get('education_university')
            skills_choices_1 = form.cleaned_data.get('skills_choices_1')
            skills_choices_2 = form.cleaned_data.get('skills_choices_2')
            skills_choices_3 = form.cleaned_data.get('skills_choices_3')
            skills_choices_4 = form.cleaned_data.get('skills_choices_4')
            skills_choices_5 = form.cleaned_data.get('skills_choices_5')
            skills_choices_6 = form.cleaned_data.get('skills_choices_6')
            skills_choices_7 = form.cleaned_data.get('skills_choices_7')
            skills_choices_8 = form.cleaned_data.get('skills_choices_8')
            skills_choices_9 = form.cleaned_data.get('skills_choices_9')
            skills_choices_10 = form.cleaned_data.get('skills_choices_10')
            uid = request.user.id
            cand = Candidate.objects.get(user_id=uid)
            cand.bio = bio
            cand.education_university = education_university
            cand.skills_choices_1 = skills_choices_1
            cand.skills_choices_2 = skills_choices_2
            cand.skills_choices_3 = skills_choices_3
            cand.skills_choices_4 = skills_choices_4
            cand.skills_choices_5 = skills_choices_5
            cand.skills_choices_6 = skills_choices_6
            cand.skills_choices_7 = skills_choices_7
            cand.skills_choices_8 = skills_choices_8
            cand.skills_choices_9 = skills_choices_9
            cand.skills_choices_10 = skills_choices_10
            cand.save()
            context = {'bio': cand.bio, 'education_university': cand.education_university,
                       'skills_choices_1': cand.skills_choices_1, 'skills_choices_6': cand.skills_choices_6,
                       'skills_choices_2': cand.skills_choices_2, 'skills_choices_7': cand.skills_choices_7,
                       'skills_choices_3': cand.skills_choices_3, 'skills_choices_8': cand.skills_choices_8,
                       'skills_choices_4': cand.skills_choices_4, 'skills_choices_9': cand.skills_choices_9,
                       'skills_choices_5': cand.skills_choices_5, 'skills_choices_10': cand.skills_choices_10,
                       }
            return render(request, 'candidates_landing.html', context)
    else:
        form = CandidateForm
    return render(request, 'candidates_edit_profile.html', {'form': form})


# Create your views here.
def candidates_landing(request):
    uid = request.user.id
    user = Candidate.objects.get(user_id=uid)
    context = {
        #'username':user.user,
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
    return render(request, 'candidates_landing.html',context)



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

    return render(request, "candidate_search_jobs.html", context)

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

def candidate_job_detail(request, job_id):
    user = request.user

    if request.method == 'POST':
        uid = request.user.id
        new = Solicitation()
        new.candidate = Candidate.objects.get(pk=uid)
        new.job = Job.objects.get(pk=job_id)
        new.created = datetime.now()
        new.save()
        uid = request.user.id
        cand = Candidate.objects.get(user_id=uid)
        job_list = Job.objects.all()
        context = {"job_list": job_list}
        return render(request, "candidate_search_jobs.html", context)
    else:
        thisjob=Job.objects.filter(pk=job_id)
        context={'job':thisjob}
        return render(request, 'candidate_job_detail.html',context)