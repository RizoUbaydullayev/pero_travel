from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("excursions/", views.ExcursionsPageView.as_view(), name="excursions_page"),
    path("tour_overview/", views.TourOverviewPageView.as_view(), name="tour_overview_page"),
    path("personal_account/", views.PersonalAccountPageView.as_view(), name="personal_account_page"),
    path("personal_account/favorites/", views.FavoritesPageView.as_view(), name="favorites"),
    path('tours/<int:tour_id>/add_to_favorites', views.add_to_favorites, name='add_to_favorites'),
    path('tours/<int:tour_id>/remove_from_favorites', views.remove_from_favorites, name='remove_from_favorites'),

]