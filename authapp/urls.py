from django.urls import path

from . import views
from .apps import AuthappConfig 

app_name = AuthappConfig.name

urlpatterns = [
    path('register/', view=views.RegisterView.as_view(), name='register'),
    path('login/', view=views.CustomLoginView.as_view(), name='login'),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
]
