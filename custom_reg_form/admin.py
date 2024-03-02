from django.contrib import admin
from .models import UserFields
import csv
from django.http import HttpResponse
from io import StringIO


class UserFieldsAdmin(admin.ModelAdmin):
    actions = ["download_csv"]
    list_display = ("user", "age", "mobile_number", "job_title")
    list_display_links = ("user", "age", "mobile_number", "job_title")
    list_filter = ("user",)
    search_fields = ("user", "age", "mobile_number", "job_title")
    list_per_page = 25

    def download_csv(self, request, queryset, *args, **kwargs):
        import csv

        f = open("some.csv", "w")
        writer = csv.writer(f)
        writer.writerow(["user", "age", "mobile_number", "job_title"])
        for s in queryset:
            writer.writerow([s.user, s.age, s.mobile_number, s.job_title])

        f.close()
        f = open("some.csv", "r")
        response = HttpResponse(f, content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=stat-info.csv"
        return response

    download_csv.short_description = "Download CSV "


admin.site.register(UserFields, UserFieldsAdmin)
