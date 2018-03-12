from django.shortcuts import render

# Create your views here.
def cadmin_landing(request):
    return render(request,'cadmin_landing.html')
def cadmin_edit_profile(request):
    return render(request, 'cadmin_edit_profile.html')
