from django import forms
from .models import Employer, Vacancy, JobApplication


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = [
            "name",
            "contact_name",
            "email",
            "phone",
            "website",
            "notes",
        ]


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            "employer",
            "title",
            "description",
            "location",
            "closing_date",
            "status",
        ]
        widgets = {"closing_date": forms.DateInput(attrs={"type": "date"})}


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "learner_name",
            "learner_email",
            "vacancy",
            "application_date",
            "status",
            "notes",
        ]
        widgets = {"application_date": forms.DateInput(attrs={"type": "date"})}
      
        error_messages = {
            "learner_email": {
                "required": "Please enter your email address.",
                "invalid": "Please enter a valid email address, for example: learner@example.com",
            },
        }