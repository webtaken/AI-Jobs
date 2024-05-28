from django.shortcuts import render


def index(request):
    print(request.htmx)
    context = {"world": "world"}
    return render(request, "app/index.html", context)


def companies(request):
    print(request.htmx)
    context = {}
    return render(request, "app/companies_leads.html", context)
