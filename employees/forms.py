from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from datetime import date

class EmployeeForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'}),
        label="Full Name"
    )

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=True,
        widget=forms.RadioSelect,
        label="Gender"
    )

    address = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Address'}),
        label="Address"
    )

    email = forms.EmailField(
        required=True,
        validators=[EmailValidator(message="Enter a valid email address.")],
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        label="Email"
    )

    education_background = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Education Background'}),
        label="Education Background"
    )

    contact = forms.CharField(
        max_length=15,
        required=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Enter a valid contact number.")],
        widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}),
        label="Contact Number"
    )

    dob_day = forms.IntegerField(
        required=True,
        min_value=1,
        max_value=31,
        widget=forms.NumberInput(attrs={'placeholder': 'Day'}),
        label="Day of Birth"
    )
    dob_month = forms.IntegerField(
        required=True,
        min_value=1,
        max_value=12,
        widget=forms.NumberInput(attrs={'placeholder': 'Month'}),
        label="Month of Birth"
    )
    dob_year = forms.IntegerField(
        required=True,
        min_value=1900,
        max_value=date.today().year,
        widget=forms.NumberInput(attrs={'placeholder': 'Year'}),
        label="Year of Birth"
    )

    nin = forms.CharField(
        max_length=14,
        required=True,
        validators=[RegexValidator(r'^[A-Z0-9]{14}$', message="NIN must be exactly 14 characters, alphanumeric.")],
        widget=forms.TextInput(attrs={'placeholder': 'National Identification Number (NIN)'}),
        label="National ID (NIN)"
    )

    def clean(self):
        cleaned_data = super().clean()
        day = cleaned_data.get('dob_day')
        month = cleaned_data.get('dob_month')
        year = cleaned_data.get('dob_year')

        try:
            date(year, month, day)
        except ValueError:
            raise ValidationError("Invalid date of birth. Please enter a valid day, month, and year.")

        return cleaned_data
