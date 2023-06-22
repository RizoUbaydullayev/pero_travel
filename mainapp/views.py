from django.views.generic import TemplateView
from mainapp import models as mainapp_models

class MainPageView(TemplateView):
    template_name = 'mainapp/main.html'


class ExcursionsPageView(TemplateView):
    template_name = 'mainapp/excursions.html'


class TourOverviewPageView(TemplateView):
    template_name = 'mainapp/tour_overview.html'

    def get_context_data(self, **kwargs):
        context = super(TourOverviewPageView, self).get_context_data(**kwargs)
        context['objects'] = mainapp_models.Tour.objects.all()
        context['tour_dates'] = mainapp_models.TourDate.objects.filter(tour=1)
        return context


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'


class RegistrationPageView(TemplateView):
    template_name = 'mainapp/registration.html'