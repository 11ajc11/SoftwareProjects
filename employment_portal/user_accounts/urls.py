from django.conf.urls import url

from . import views as core_views

app_name = 'user_accounts'
urlpatterns = [
    url(r'^candidatesignup/', core_views.candidatesignup, name='candidatesignup'),
    url(r'^companysignup/', core_views.companysignup, name='companysignup'),
    url(r'^candidatelogin/', core_views.candidatelogin, name='candidatelogin'),
    url(r'^companylogin/', core_views.companylogin, name='companylogin'),
    url(r'^recruiterlogin/', core_views.recruiterlogin, name='recruiterlogin'),

]
