from django import forms
from .models import Voter

class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = [
            'first_name',
            'last_name',
            'gender',
            'email',
            'phone',
            'address_line_1',
            'address_line_2',
            'village',
            'state',
            'local_gov_area',
            'postal_code',
            'country',
            'date_of_birth',
            'photo',
            'is_registered',
            'is_eligible',
            'willing_to_register',
            'political_party',
            'channel'
        ]

    # function to loop through form fields and initiat form-control class
    def __init__(self, *args, **kwargs):
        super(VoterForm, self).__init__(*args, **kwargs) # modify what django is giving
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['gender'].empty_label = 'Select Gender'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['address_line_1'].widget.attrs['placeholder'] = 'Address Line 1'
        self.fields['address_line_2'].widget.attrs['placeholder'] = 'Address Line 2'
        self.fields['village'].widget.attrs['placeholder'] = 'Enter village'

        self.fields['state'].empty_label = 'Select state'
        self.fields['local_gov_area'].empty_label = 'Select LGA'

        self.fields['postal_code'].widget.attrs['placeholder'] = 'Enter postal_code'
        self.fields['country'].widget.attrs['placeholder'] = 'Enter country'

        self.fields['photo'].widget.attrs['placeholder'] = 'Upload Photo'
        self.fields['is_registered'].widget.attrs['placeholder'] = 'is_registered'
        self.fields['is_eligible'].widget.attrs['placeholder'] = 'is_eligible'
        self.fields['willing_to_register'].widget.attrs['placeholder'] = 'willing_to_register'
        self.fields['political_party'].empty_label = 'Select political_party'
        self.fields['channel'].empty_label = 'Select channel'

        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'Enter Date of Birth'
        self.fields['date_of_birth'].input_formats = '%d-%m-%Y %H:%M:%S'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control datetimepicker'

        for field in ('first_name', 'last_name', 'email', 'phone', 'address_line_1', 'address_line_2', 'village', 'local_gov_area', 'state', 'postal_code', 'country', 'photo', 'is_registered', 'is_eligible', 'willing_to_register', 'political_party', 'channel'):
            self.fields[field].widget.attrs['class'] = 'form-control'

        for field in ('is_registered', 'is_eligible', 'willing_to_register'):
            self.fields[field].widget.attrs['class'] = 'django-checkbox'

class PreRegisterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = [
            'first_name',
            'last_name',
            'gender',
            'phone',
            'local_gov_area',
            'state',
            'date_of_birth',
            'channel'
        ]

    # function to loop through form fields and initiat form-control class
    def __init__(self, *args, **kwargs):
        super(PreRegisterForm, self).__init__(*args, **kwargs) # modify what django is giving
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['gender'].empty_label = 'Select Gender'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['state'].empty_label = 'Select state'
        self.fields['local_gov_area'].empty_label = 'Select LGA'
        self.fields['channel'].empty_label = 'Select channel'

        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'Enter Date of Birth'
        self.fields['date_of_birth'].input_formats = '%d-%m-%Y %H:%M:%S'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control datetimepicker'

        for field in ('first_name', 'last_name', 'gender', 'phone', 'local_gov_area', 'state', 'channel'):
            self.fields[field].widget.attrs['class'] = 'form-control'
