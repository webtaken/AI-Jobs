from django.shortcuts import render


def index(request):
    print(request.htmx)
    context = {"name": "world"}
    return render(request, "app/index.html", context)
