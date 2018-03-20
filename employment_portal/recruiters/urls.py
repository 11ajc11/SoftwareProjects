from django.conf.urls import url

from . import views as core_views

app_name = 'recruiters'
urlpatterns = [
    url(r'^recruiters_landing/', core_views.recruiters_landing, name='recruiters_landing'),
    url(r'^recruiters_postings/', core_views.recruiters_postings, name='recruiters_postings'),
    url(r'^recruiters_sent_offers/', core_views.recruiters_sent_offers, name='recruiters_sent_offers'),
    url(r'^recruiters_smart_match/(?P<job_id>[0-9]+)/', core_views.recruiters_smart_match, name='recruiters_smart_match'),
    url(r'^recruiter_cand_detail/(?P<cand_id>[0-9]+)/(?P<job_id>[0-9]+)/', core_views.recruiter_cand_detail, name='recruiter_cand_detail'),
    url(r'^recruiters_view_post/', core_views.recruiters_view_post, name='recruiters_view_post'),
    url(r'^recruiters_view_solicitations/', core_views.recruiters_view_solicitations, name='recruiters_view_solicitations'),
    url(r'^', core_views.recruiter_logout, name='recruiter_logout'),
]
