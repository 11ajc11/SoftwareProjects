"""employment_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.homez, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^user_accounts/', include('user_accounts.urls')),
    url(r'^candidates/', include('candidates.urls')),
    url(r'^company/', include('company.urls')),
    #url(r'^offer_solicit/', include('offer_solicit.urls')),
    #url(r'^postings/', include('postings.urls')),
    url(r'^recruiters/', include('recruiters.urls')),
]
