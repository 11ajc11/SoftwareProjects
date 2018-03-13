from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import CompanyForm

# Create your views here.
def cadmin_landing(request):
    return render(request,'cadmin_landing.html')

class cadmin_edit_profile(FormView):
    template_name = 'cadmin_edit_profile.html'
    form_class = CompanyForm

    '''def form_valid(self, form):
        form.save()
        messages.success(self.request, "Profile Saved")
        return render(self.request, 'success.html', self.get_context_data())'''

def cadmin_edit_profile(request):
     return render(request, 'cadmin_edit_profile.html')

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
