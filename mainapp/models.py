from pathlib import Path
from time import time
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


def tour_photos_path(instance, filename):
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return f'tours/{instance.type}/{datetime.now().month}/pic_{num}{suff}'


# class Attraction(models.Model):
#     tour = models.ForeignKey()
#     description = models.CharField(
#         max_length=256, verbose_name=_("Attraction description"))
#     to_choose_from = models.BooleanField(default=False)
#     county_name = models.CharField(max_length=50, verbose_name=_(
#         "The name of the county where the attraction is located"))
#     image = models.ImageField(
#         upload_to=tour_photos_path, verbose_name=_("Attraction photo "))


# class Expense(models.Model):
#     name = models.CharField(max_length=40, verbose_name=_('Expense name'))
#     price = models.PositiveIntegerField(
#         blank=True, verbose_name=_("Expense price"))


# class ImportantInformation(models.Model):
#     description = models.CharField(max_length=256, verbose_name=_(
#         'Important information when crossing the border'))


class TourType(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Tour type name"))

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=256, verbose_name=_('Tour name'))
    type = models.ForeignKey(
        TourType, on_delete=models.CASCADE, verbose_name=_("Tour type"))
    description = models.TextField(verbose_name=_("Tour description"))
    seat = models.PositiveSmallIntegerField(verbose_name=_("Number of seats"))
    main_image = models.ImageField(
        upload_to=tour_photos_path, verbose_name=_("Tour main image"))
    child_ticket = models.PositiveIntegerField(
        verbose_name=_("Child ticket price"))
    adult_ticket = models.PositiveIntegerField(
        verbose_name=_("Adult ticket price"))
    duration = models.DecimalField(
        max_digits=3, decimal_places=1, verbose_name=_("Tour duration in hours"))
    calendar_image = models.ImageField(
        upload_to=tour_photos_path, verbose_name=_("Image for calendar"))
    # attractions = models.ForeignKey(Attraction, on_delete=models.CASCADE, verbose_name=_("Visited attractions included in the tour"))
    # additional_expenses = models.ForeignKey(Expense, on_delete=models.CASCADE, verbose_name=_("Additional expenses"))
    # important_informations = models.ForeignKey(ImportantInformation, on_delete=models.CASCADE, verbose_name=_("Important information when crossing the border"))
    # photo_galleries = models.ImageField(upload_to=tour_photos_path, verbose_name=_("Images for gallery"))

    def __str__(self):
        return self.name


class TourDate(models.Model):
    date = models.DateField(verbose_name=_('Tour date'))
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
