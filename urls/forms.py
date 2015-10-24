from django.contrib.auth import forms
from django.forms import CharField


class BootstrapAuthenticationForm(forms.AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(BootstrapAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
