from django.conf.urls import url
from . import views as core_views

app_name = 'company'
urlpatterns = [
    url(r'^cadmin_landing/', core_views.cadmin_landing, name='cadmin_landing'),
    url(r'^cadmin_edit_profile/', core_views.cadmin_edit_profile, name='cadmin_edit_profile'),
    url(r'^cadmin_add_posting/', core_views.cadmin_add_posting, name='cadmin_add_posting'),
    url(r'^cadmin_add_recruiter/', core_views.cadmin_add_recruiter, name='cadmin_add_recruiter'),
    url(r'^cadmin_edit_posting/', core_views.cadmin_edit_posting, name='cadmin_edit_posting'),
    url(r'^cadmin_edit_recruiter/', core_views.cadmin_edit_recruiter, name='cadmin_edit_recruiter'),
    url(r'^cadmin_view_postings/', core_views.cadmin_view_postings, name='cadmin_view_postings'),
    url(r'^cadmin_view_recruiters/', core_views.cadmin_view_recruiters, name='cadmin_view_recruiters'),
]
