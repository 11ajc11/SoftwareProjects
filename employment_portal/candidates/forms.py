from .models import Candidate, CandidateSkills
from django.forms import ModelForm,Textarea
from django.utils.translation import gettext_lazy as _



class CandidateForm(ModelForm):
    class Meta:
        model = Candidate

        fields = ('bio', 'education_university','skills_choices_1','skills_choices_2','skills_choices_3',
                  'skills_choices_4', 'skills_choices_5', 'skills_choices_6', 'skills_choices_7',
                  'skills_choices_8', 'skills_choices_9', 'skills_choices_10')
        widgets={'bio':Textarea(attrs={'cols':40,'rows':15})}
        labels = {
            'bio': _('Bio'),
            'education_university': _('School'),
        }
        help_texts = {
            'bio': _('Give a brief description about you.'),
        }
        error_messages = {
            'bio' :{
                'max_length': _("This bio is too long.")
            },
        }
