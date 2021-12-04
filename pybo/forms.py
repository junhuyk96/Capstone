from django import forms
from pybo.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name', 'email', 'phone', 'message']
        labels = {
            'name': 'FULL NAME',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'message': 'Message'
        }