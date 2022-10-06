from django.urls import path
from . import views

# ######:8000/people/
urlpatterns = [
    path('', views.simple_view)
]
