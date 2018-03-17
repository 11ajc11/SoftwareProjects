from django.shortcuts import render

def recruiters_landing(request):
    return render(request,"recruiters_landing.html")
    
def recruiters_postings(request):
    return render(request,"recruiters_postings.html")
def recruiters_sent_offers(request):
    return render(request,"recruiters_sent_offers.html")
def recruiters_smart_match(request):
    return render(request,"recruiters_smart_match.html")
def recruiters_view_post(request):
    return render(request,"recruiters_view_post.html")
def recruiters_view_solicitations(request):
    return render(request,"recruiters_view_solicitations.html")
