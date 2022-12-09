from django import forms
from .models import Lead

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'full_name',
            'email',
            'job_title',
            'company_name',
            'involvement',
            'program',
            'message',
            'channel'
         ]
    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        self.fields['program'].empty_label = 'Select program your interested in'

        self.fields['full_name'].widget.attrs['placeholder'] = 'Enter Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['job_title'].widget.attrs['placeholder'] = 'Enter Job Title'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Enter Company Name'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter Message'
        self.fields['message'].widget.attrs['rows'] = 3

        for field in ('full_name', 'email', 'job_title', 'company_name', 'involvement', 'program', 'message', 'channel'):
            self.fields[field].widget.attrs['class'] = 'form-control'
