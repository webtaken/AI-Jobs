from django.contrib import admin

from .models import AlertEmail, CompanyEmail


class CompanyEmailAdmin(admin.ModelAdmin):
    list_display = ["company_name", "email", "url", "country"]


admin.site.register(AlertEmail)
admin.site.register(CompanyEmail, CompanyEmailAdmin)
