from django.db import models

# Create your models here.


class Employer(models.Model):
    name = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


class Vacancy(models.Model):
    class Status(models.TextChoices):
        OPEN = "Open", "Open"
        CLOSED = "Closed", "Closed"
        ON_HOLD = "On hold", "On hold"

    employer = models.ForeignKey(
        Employer,
        on_delete=models.PROTECT,
        related_name="vacancies",
    )
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    closing_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
    )

    def __str__(self):
        return f"{self.title} - {self.employer.name}"


class JobApplication(models.Model):
    class Status(models.TextChoices):
        DRAFT = "Draft", "Draft"
        APPLIED = "Applied", "Applied"
        INTERVIEW = "Interview", "Interview"
        OFFER = "Offer", "Offer"
        REJECTED = "Rejected", "Rejected"
        WITHDRAWN = "Withdrawn", "Withdrawn"

    learner_name = models.CharField(max_length=150)
    learner_email = models.EmailField(blank=True)
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.PROTECT,
        related_name="applications",
    )
    application_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.learner_name} - {self.vacancy.title}"  # pylint: disable=no-member
        )


# Create your models here.
