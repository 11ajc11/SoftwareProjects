from django.conf.urls import url

from . import views as core_views

app_name = 'company'
urlpatterns = [
    url(r'^cadmin_landing/', core_views.cadmin_landing, name='cadmin_landing'),
    url(r'^cadmin_edit_profile/', core_views.cadmin_edit_profile, name='cadmin_edit_profile')
]
