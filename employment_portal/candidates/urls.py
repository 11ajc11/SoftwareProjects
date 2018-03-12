from django.conf.urls import url

from . import views as core_views

app_name = 'candidates'
urlpatterns = [
    url(r'^candidates_landing/', core_views.candidates_landing, name='candidates_landing'),
    url(r'^candidates_edit_profile/', core_views.candidates_edit_profile, name='candidates_edit_profile')
]
