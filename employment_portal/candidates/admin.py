from allauth.account.utils import user_email
from django.contrib import admin
# Register your models here.
from .models import CandidateSkills, CandidateResume, Candidate
from offer_solicit.models import Solicitation
from user_accounts.models import UserProfile


class SolicitationRequestInLine(admin.StackedInline):
    model = Solicitation
class CandidateSkillsInLine(admin.StackedInline):
    model = CandidateSkills
class CandidateResumeInLine(admin.StackedInline):
    model = CandidateResume
class CandidateAdmin(admin.ModelAdmin):
    def email(obj):
        return '%s' % (obj.user.email)
    email.admin_order_field = 'user_email'
    def name(obj):
        return ('%s' % (obj.user.get_full_name()))
    def date_of_birth(obj):
        return ('%s' % (obj.date_of_birth or obj.birth_year))
    date_of_birth.admin_order_field = 'date_of_birth'
    # inlines = (CandidateRequirementsInline,)
    list_display = (email, name, date_of_birth, 'gender')
    inlines = (CandidateResumeInLine, SolicitationRequestInLine)
    exclude = ('password', 'last_login', 'is_admin', 'thumb')
    search_fields = ('date_of_birth', 'birth_year', 'user__email',
        'user__first_name', 'user__last_name',)

admin.site.register(Candidate, CandidateAdmin)