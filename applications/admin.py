from django.contrib import admin
from .models import Employer, Vacancy, JobApplication

# Register your models here.
admin.site.register(Employer)
admin.site.register(Vacancy)
admin.site.register(JobApplication)
