from django.conf.urls import url
from . import views as core_views

app_name = 'candidates'
urlpatterns = [
    url(r'^candidates_landing/', core_views.candidates_landing, name='candidates_landing'),
    url(r'^candidates_edit_profile/', core_views.candidates_edit_profile.as_view(), name='candidates_edit_profile'),
    url(r'^candidate_login/', core_views.candidate_login, name='candidate_login'),
    url(r'^candidate_search_companies/', core_views.candidate_search_companies, name='candidate_search_companies'),
    url(r'^candidate_search_jobs/', core_views.candidate_search_jobs, name='candidate_search_jobs'),
    #url(r'^candidates_sign_up/', core_views.candidates_landing, name='candidates_landing'),
    url(r'^candidate_smart_search/', core_views.candidate_smart_search, name='candidate_smart_search'),
    url(r'^candidate_solicit/', core_views.candidate_solicit, name='candidate_solicit'),
    url(r'^candidate_offers/', core_views.candidate_offers, name='candidate_offers'),
    url(r'^candidateeditprofile/', core_views.candidateeditprofileview.as_view(), name = 'candidateeditprofile'),
]
