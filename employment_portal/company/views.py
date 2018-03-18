from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import CompanyForm, AddPostingForm,AddRecruiterForm
from .models import Employer
from recruiters.models import Recruiter
from postings.models import Job
from user_accounts.models import UserProfile
from django.contrib.auth import authenticate



#Create your views here.
def cadmin_landing(request):
    uid = request.user.id
    employer=Employer.objects.get(user_id=uid)
    temp=employer.website.replace('http://','');
    context={'bio':employer.bio,'name':employer.name_english,'website':temp}

    return render(request,'cadmin_landing.html',context)

def cadmin_edit_profile(request):
    #template_name = 'cadmin_edit_profile.html'
    #form_class = CompanyForm
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            website = form.cleaned_data.get('website')
            bio = form.cleaned_data.get('bio')
            CompanyName=form.cleaned_data.get('name_english')
            uid = request.user.id
            cand = Employer.objects.get(user_id=uid)
            cand.website = website
            cand.bio = bio
            cand.name_english=CompanyName
            cand.save()
            temp=cand.website.replace('http://','');
            context = {'bio': cand.bio, 'name':cand.name_english, 'website': temp}
            return render(request, 'cadmin_landing.html', context)
    else:
        form = CompanyForm
    return render(request, 'cadmin_edit_profile.html', {'form':form})


    '''def form_valid(self, form):
        form.save()
        messages.success(self.request, "Profile Saved")
        return render(self.request, 'success.html', self.get_context_data())'''

#def cadmin_edit_profile(request):
     #return render(request, 'cadmin_edit_profile.html')

def cadmin_add_posting(request):
    if request.method == 'POST':
        print('yeahdude')
        form = AddPostingForm(request.POST)
        if form.is_valid():
            job_title = form.cleaned_data.get('job_title')
            Job_Description = form.cleaned_data.get('Job_Description')
            recruiter=form.cleaned_data.get('recruiter')
            job_skills_1=form.cleaned_data.get('job_skills_1')
            job_skills_2=form.cleaned_data.get('job_skills_2')
            job_skills_3=form.cleaned_data.get('job_skills_3')
            job_skills_4=form.cleaned_data.get('job_skills_4')
            job_skills_5=form.cleaned_data.get('job_skills_5')
            job_skills_6=form.cleaned_data.get('job_skills_6')
            job_skills_7=form.cleaned_data.get('job_skills_7')
            job_skills_8=form.cleaned_data.get('job_skills_8')
            job_skills_9=form.cleaned_data.get('job_skills_9')
            job_skills_10=form.cleaned_data.get('job_skills_10')

            uid = request.user.id
            employer=Employer.objects.get(user_id=uid)
            posting = Job()
            posting.job_title=job_title
            posting.Job_Description=Job_Description
            #posting.recruiter=recruiter
            posting.job_skills_1=job_skills_1
            posting.job_skills_2=job_skills_2
            posting.job_skills_3=job_skills_3
            posting.job_skills_4=job_skills_4
            posting.job_skills_5=job_skills_5
            posting.job_skills_6=job_skills_6
            posting.job_skills_7=job_skills_7
            posting.job_skills_8=job_skills_8
            posting.job_skills_9=job_skills_9
            posting.job_skills_10=job_skills_10
            posting.Employer_Name=employer
            posting.weekly_hours=40;
            posting.save()

            return render(request, 'cadmin_view_postings.html')
    else:
        print('nahdude')
        form = AddPostingForm
    return render(request, 'cadmin_add_posting.html',{'form':form})

def cadmin_add_recruiter(request):
    if request.method=='POST':
        form = AddRecruiterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            p = UserProfile()
            p.user_type='recruiter'
            p.user = user
            p.save()
            uid = request.user.id
            employer=Employer.objects.get(user_id=uid)
            recruiter = Recruiter()
            recruiter.user = user
            recruiter.education = 'Depaul'
            recruiter.date_of_birth = '1223-3-2'
            recruiter.Employer_Name=employer
            recruiter.save()
            return redirect('company:cadmin_view_recruiters')
    else:
        form = AddRecruiterForm()
    return render(request, 'cadmin_add_recruiter.html',{'form':form})

def cadmin_edit_posting(request):
    return render(request,'cadmin_edit_posting.html')

def cadmin_edit_recruiter(request):
    return render(request, 'cadmin_edit_recruiter.html')

def cadmin_view_postings(request):
    uid = request.user.id
    posting_list=Job.objects.filter(Employer_Name__user_id=uid)
    context={'posting_list':posting_list}
    return render(request, 'cadmin_view_postings.html',context)

def cadmin_view_recruiters(request):
    uid = request.user.id
    recruiter_list=Recruiter.objects.filter(Employer_Name__user_id=uid)
    context={'recruiter_list':recruiter_list}
    return render(request, 'cadmin_view_recruiters.html',context)
