from .models import Employer
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _


class CompanyForm(ModelForm):
    class Meta:
            model = Employer
            fields = ('bio', 'website')
            labels = {
                'bio': _('Bio'),
                'website': _('Website'),
            }
            help_texts = {
                'bio': _('Give a brief description about you.'),
            }
            error_messages = {
                'bio': {
                    'max_length': _("This bio is too long.")
                },
            }
            widgets={'bio' : Textarea (attrs={'cols':40,'rows':15})}
    """class Meta:
        model=Employer
        fields = ['bio', 'website']
        widgets={'bio' : Textarea ( attrs={'value' : model.bio} ),
                   'website': Textarea(attrs={'value': model.website})}"""
