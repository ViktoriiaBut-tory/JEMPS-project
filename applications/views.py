from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Employer, Vacancy, JobApplication
from .forms import EmployerForm


# protected views
@login_required
def dashboard(request):
    return render(
        request,
        "dashboard.html",
        {
            "employer_count": Employer.objects.count(),
            "vacancy_count": Vacancy.objects.count(),
            "application_count": JobApplication.objects.count(),
        },
    )


@login_required
def employer_list(request):
    return render(
        request,
        "employers/list.html",
        {
            "employers": Employer.objects.all(),
        },
    )


@login_required
def vacancy_list(request):
    return render(
        request,
        "vacancies/list.html",
        {
            "vacancies": Vacancy.objects.select_related("employer"),
        },
    )


@login_required
def application_list(request):
    return render(
        request,
        "applications/list.html",
        {
            "applications": JobApplication.objects.select_related(
                "vacancy", "vacancy__employer"
            ),
        },
    )


# protected views ends


class EmployerCreateView(LoginRequiredMixin, CreateView):
    model = Employer
    form_class = EmployerForm
    template_name = "employers/form.html"
    success_url = reverse_lazy("employer_list")

    def form_valid(self, form):
        messages.success(self.request, "Employer added successfully.")
        return super().form_valid(form)


class EmployerUpdateView(LoginRequiredMixin, UpdateView):
    model = Employer
    form_class = EmployerForm
    template_name = "employers/form.html"
    success_url = reverse_lazy("employer_list")

    def form_valid(self, form):
        messages.success(self.request, "Employer updated successfully.")
        return super().form_valid(form)


class EmployerDeleteView(LoginRequiredMixin, DeleteView):
    model = Employer
    template_name = "employers/confirm_delete.html"
    success_url = reverse_lazy("employer_list")
