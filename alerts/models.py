from django.db.models import CharField, EmailField, URLField

from commons.models import TimeStampedModel


class AlertEmail(TimeStampedModel):
    email = EmailField(unique=True)

    def __str__(self):
        return f"{self.email}"


class CompanyEmail(TimeStampedModel):
    company_name = CharField(max_length=100)
    email = EmailField(unique=True)
    url = URLField()
    country = CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.company_name} - {self.email} ({self.country})"
