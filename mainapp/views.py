from typing import Any
from django import http
from django.views.generic import TemplateView, View
from mainapp import models as mainapp_models
from django.views.decorators.csrf import csrf_exempt


def add_to_favorites(request, tour_id):
    tour = mainapp_models.Tour.objects.get(pk=tour_id)
    if tour in request.user.favorite_tours.all():
        return http.JsonResponse({'status': 'error', 'message': 'Тур уже добавлен в избранное.'})
    request.user.favorite_tours.add(tour)
    data = {'result': 'success','tour_id': tour_id, 'message': 'Тур успешно добавлен в избранное.'}
    return http.JsonResponse(data)


def remove_from_favorites(request, tour_id):
    tour = mainapp_models.Tour.objects.get(pk=tour_id)

    if tour not in request.user.favorite_tours.all():
        return http.JsonResponse({'status': 'error', 'message': 'Тура нету в избранном.'})
    
    request.user.favorite_tours.remove(tour)
    data = {'result': 'success','tour_id': tour_id,'message': 'Тур успешно удален из избранного.'}
    return http.JsonResponse(data)


class MainPageView(TemplateView):
    template_name = 'mainapp/main.html'


class ExcursionsPageView(TemplateView):
    template_name = 'mainapp/excursions.html'

    def get_context_data(self, **kwargs):
        context = super(ExcursionsPageView, self).get_context_data(**kwargs)
        context['objects'] = mainapp_models.Tour.objects.all()
        context['favorite_tours'] = self.request.user.favorite_tours.all()
        for tour in context['objects']:
            if tour.duration == int(tour.duration):
                tour.duration = int(tour.duration)
        return context


class TourOverviewPageView(TemplateView):
    template_name = 'mainapp/tour_overview.html'

    def get_context_data(self, **kwargs):
        context = super(TourOverviewPageView, self).get_context_data(**kwargs)
        # context['objects'] = mainapp_models.Tour.objects.all()
        # context['tour_dates'] = mainapp_models.TourDate.objects.filter(tour=1)
        return context


class PersonalAccountPageView(TemplateView):
    template_name = 'mainapp/personal_account.html'


class FavoritesPageView(TemplateView):
    template_name = 'mainapp/favorites.html'
    def get_context_data(self, **kwargs):
        context = super(FavoritesPageView, self).get_context_data(**kwargs)
        context['favorite_tours'] = self.request.user.favorite_tours.all()
        return context
    
