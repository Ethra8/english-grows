from django import forms
from .models import CompanyContact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import CompanyContact


class CompanyContactForm(forms.ModelForm):
    """
    Add placeholders and classes, remove auto-generated
    labels, and set autofocus on first field
    """
    class Meta:
        model = CompanyContact
        fields = '__all__'
    
    # Customizing the 'message' field's widget
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3,  # Limit the number of rows to 4
                'placeholder': 'Enter your message here...',  # Optional: Add placeholder text
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CompanyContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
