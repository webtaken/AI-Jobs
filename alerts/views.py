from django.http import HttpRequest, HttpResponse

from .models import AlertEmail, CompanyEmail


def set_alert(request: HttpRequest):
    email = request.POST.get("email", None)
    if email is None or email.strip() == "":
        return HttpResponse(
            '<p class="text-center text-error">:( Please provide an email address.</p>'
        )

    _, _ = AlertEmail.objects.get_or_create(email=email)

    return HttpResponse(
        '<p class="text-center text-success">We&apos;ll contact you soon!</p>'
    )


def lead_company(request: HttpRequest):
    company_name = request.POST.get("company_name", None)
    email = request.POST.get("email", None)
    company_url = request.POST.get("company_url", None)
    country = request.POST.get("country", None)

    if company_name is None or company_name.strip() == "":
        return HttpResponse(
            '<p class="text-center text-error">:( Please provide your company name.</p>'
        )
    if email is None or email.strip() == "":
        return HttpResponse(
            '<p class="text-center text-error">:( Please provide your email address.</p>'
        )
    if company_url is None or company_url.strip() == "":
        return HttpResponse(
            '<p class="text-center text-error">:( Please provide your company URL.</p>'
        )
    if country is None or country.strip() == "":
        return HttpResponse(
            '<p class="text-center text-error">:( Please provide your country or location.</p>'
        )

    _, _ = CompanyEmail.objects.get_or_create(
        email=email,
        defaults={
            "company_name": company_name,
            "email": email,
            "url": company_url,
            "country": country,
        },
    )

    return HttpResponse(
        '<p class="text-center text-success">We&apos;ll contact you soon!</p>'
    )
