from django.shortcuts import render

# Create your views here.
def cadmin_landing(request):
    return render(request,'cadmin_landing.html')

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
