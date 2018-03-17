from .models import Employer
from postings.models import Job
from django.forms import ModelForm, Textarea,TextInput,ChoiceField
from django.utils.translation import gettext_lazy as _



class CompanyForm(ModelForm):
    class Meta:
            model = Employer
            fields = ('name_english','bio', 'website',)
            labels = {
                'bio': _('Bio'),
                'website': _('Website'),
                'name_english':_('Company Name'),
            }

            error_messages = {
                'bio': {
                    'max_length': _("This bio is too long.")
                },
            }
            widgets={'bio' : Textarea (attrs={'cols':40,'rows':15,'class':"input-group-text"}),'name_english' : TextInput (attrs={'cols':50,'rows':1,'class':"input-group-text"}),'website' : TextInput (attrs={'cols':40,'rows':1, 'class':"mb-4 w-100 input-group-text"})}

class AddPostingForm(ModelForm):
    class Meta:
            model = Job
            fields = ('job_title','Job_Description', 'job_skills_1','job_skills_2',
            'job_skills_3','job_skills_4','job_skills_5','job_skills_6','job_skills_7',
            'job_skills_8','job_skills_9','job_skills_10')
            labels = {
                'job_title': _('Job Title'),
                'Job_Description': _('Job Description'),
                'job_skills_1': _('Skill 1'),
                'job_skills_2':_('Skill 2'),
                'job_skills_3': _('Skill 3'),
                'job_skills_4': _('Skill 4'),
                'job_skills_5':_('Skill 5'),
                'job_skills_6': _('Skill 6'),
                'job_skills_7': _('Skill 7'),
                'job_skills_8':_('Skill 8'),
                'job_skills_9': _('Skill 9'),
                'job_skills_10': _('Skill 10'),
            }
            error_messages = {
                'Job_Description': {
                    'max_length': _("This bio is too long.")
                },
            }
            widgets={
            'Job_Description' : Textarea (attrs={'cols':40,'rows':15,}),
            'job_title' : TextInput (attrs={'cols':40,'rows':1,}),
            #'recruiter' : ChoiceField (),
            # 'job_skills_1' : ChoiceField (),
            # 'job_skills_2' : ChoiceField (),
            # 'job_skills_3' : ChoiceField (),
            # 'job_skills_4' : ChoiceField (),
            # 'job_skills_5' : ChoiceField (),
            # 'job_skills_6' : ChoiceField (),
            # 'job_skills_7' : ChoiceField (),
            # 'job_skills_8' : ChoiceField (),
            # 'job_skills_9' : ChoiceField (),
            # 'job_skills_10' : ChoiceField (),
            }



    """class Meta:
        model=Employer
        fields = ['bio', 'website']
        widgets={'bio' : Textarea ( attrs={'value' : model.bio} ),
                   'website': Textarea(attrs={'value': model.website})}"""
