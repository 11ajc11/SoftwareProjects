from django.shortcuts import render

# Create your views here.
def candidates_landing(request):
    return render(request,"candidates_landing.html")
def candidates_edit_profile(request):
    return render(request,"candidates_edit_profile.html")
