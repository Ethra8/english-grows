from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels, and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Update Profile'))
        
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_country': 'Country',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        
        for field in self.fields:
            if field != 'default_country':  # CountryField does not need a placeholder
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False