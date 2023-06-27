from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


class TourDateInline(admin.TabularInline):
    model = mainapp_models.TourDate
    extra = 1


class AttractionInline(admin.TabularInline):
    model = mainapp_models.Attraction


class ExpenseInline(admin.TabularInline):
    model = mainapp_models.Expense


class ImportantInformationInline(admin.TabularInline):
    model = mainapp_models.ImportantInformation


class PhotoGalleryInline(admin.TabularInline):
    model = mainapp_models.PhotoGallery


@admin.register(mainapp_models.Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourDateInline, AttractionInline, ExpenseInline,
               ImportantInformationInline, PhotoGalleryInline]
    list_display = ['name', 'type', 'child_ticket',
                    'adult_ticket', 'display_dates']

    def display_dates(self, obj):
        dates = mainapp_models.TourDate.objects.filter(tour=obj)
        return ' , '.join([str(date.date) for date in dates])

    def display_attractions(self, obj):
        attractions = mainapp_models.Attraction.objects.filter(tour=obj)
        return ' , '.join([attraction.description for attraction in attractions])

    def display_expenses(self, obj):
        expenses = mainapp_models.Expense.objects.filter(tour=obj)
        return ' , '.join([expense.name for expense in expenses])

    def display_important_information(self, obj):
        important_informations = mainapp_models.ImportantInformation.objects.filter(
            tour=obj)
        return ' , '.join([important_information.description for important_information in important_informations])

    def display_photo_gallery(self, obj):
        photos = mainapp_models.PhotoGallery.objects.filter(tour=obj)
        return ' , '.join([photo.photo.url for photo in photos])

    display_dates.short_description = 'Dates'
    display_attractions.short_description = 'Attractions'
    display_expenses.short_description = 'Expenses'
    display_important_information.short_description = 'Important information'
    display_photo_gallery.short_description = 'Photos'


@admin.register(mainapp_models.TourType)
class TourTypeAdmin(admin.ModelAdmin):
    pass
