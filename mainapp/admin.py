from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


class TourDateInline(admin.TabularInline):
    model = mainapp_models.TourDate
    extra = 1


# class AttractionInline(admin.TabularInline):
#     model = mainapp_models.Attraction


# class ExpenseInline(admin.TabularInline):
#     model = mainapp_models.Expense


# class ImportantInformationInline(admin.TabularInline):
#     model = mainapp_models.ImportantInformation

@admin.register(mainapp_models.Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourDateInline]
    list_display = ['name', 'type', 'child_ticket', 'adult_ticket', 'display_dates']

    def display_dates(self, obj):
        dates = mainapp_models.TourDate.objects.filter(tour=obj)
        return ', '.join([date.date.strftime("%Y-%m-%d") for date in dates])
    
    display_dates.short_description = 'Dates'


@admin.register(mainapp_models.TourType)
class TourTypeAdmin(admin.ModelAdmin):
    pass