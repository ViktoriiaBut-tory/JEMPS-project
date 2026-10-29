from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("employers/", views.employer_list, name="employer_list"),
    path("vacancies/", views.vacancy_list, name="vacancy_list"),
    path("applications/", views.application_list, name="application_list"),
    path("employers/add/", views.EmployerCreateView.as_view(), name="employer_add"),
    path(
        "employers/<int:pk>/edit/",
        views.EmployerUpdateView.as_view(),
        name="employer_edit",
    ),
    path(
        "employers/<int:pk>/delete/",
        views.EmployerDeleteView.as_view(),
        name="employer_delete",
    ),
    path(
        "vacancies/add/",
        views.VacancyCreateView.as_view(),
        name="vacancy_add",
    ),
    path(
        "vacancies/<int:pk>/edit/",
        views.VacancyUpdateView.as_view(),
        name="vacancy_edit",
    ),
    path(
        "vacancies/<int:pk>/delete/",
        views.VacancyDeleteView.as_view(),
        name="vacancy_delete",
    ),
]
