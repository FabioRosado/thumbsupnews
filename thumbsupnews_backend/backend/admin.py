from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import Headline, Contact

# Register your models here.
TokenAdmin.raw_id_fields = ["user"]


def make_positive(modeladmin, request, queryset):
    queryset.update(is_positive=True)
    make_positive.short_description = "Mark selected headlines positive"


class HeadlineAdmin(admin.ModelAdmin):
    list_display = ["title", "categories", "sentiment", "is_positive", "date"]
    list_filter = ["date"]
    actions = [make_positive]
    ordering = ["-date"]


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message"]


admin.site.register(Headline, HeadlineAdmin)
admin.site.register(Contact, ContactAdmin)
