from django.urls import path  # type: ignore
from .views import *
urlpatterns = [
    path('home/', Homepage)
    ]