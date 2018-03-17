from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import CompanyForm
from .models import Employer

# Create your views here.
def cadmin_landing(request):
    uid = request.user.id
    employer=Employer.objects.get(user_id=uid)
    context={'bio':employer.bio,'name':employer.user,'website':employer.website}
    return render(request,'cadmin_landing.html',context)

def cadmin_edit_profile(request):
    #template_name = 'cadmin_edit_profile.html'
    #form_class = CompanyForm
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            website = form.cleaned_data.get('website')
            bio = form.cleaned_data.get('bio')
            uid = request.user.id
            cand = Employer.objects.get(user_id=uid)
            cand.website = website
            cand.bio = bio
            cand.save()
            pass
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
    return render(request, 'cadmin_add_posting.html')

def cadmin_add_recruiter(request):
    return render(request, 'cadmin_add_recruiter.html')

def cadmin_edit_posting(request):
    return render(request,'cadmin_edit_posting.html')

def cadmin_edit_recruiter(request):
    return render(request, 'cadmin_edit_recruiter.html')

def cadmin_view_postings(request):
    return render(request, 'cadmin_view_postings.html')

def cadmin_view_recruiters(request):
    return render(request, 'cadmin_view_recruiters.html')
