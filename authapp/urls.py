from django.urls import path

from . import views
from .apps import AuthappConfig 

app_name = AuthappConfig.name

urlpatterns = [
    path('register/', view=views.RegisterView.as_view(), name='register')
]
