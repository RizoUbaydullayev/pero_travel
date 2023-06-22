from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("excursions/", views.ExcursionsPageView.as_view(), name="excursions_page"),
    path("tour_overview/", views.TourOverviewPageView.as_view(), name="tour_overview_page"),
    path("login/", views.LoginPageView.as_view(), name="login_page"),
    path("registration/", views.RegistrationPageView.as_view(), name="registration_page"),
]