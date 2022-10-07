from django.urls import path
from .views import NewPersonBattleListView, PersonHomeView, PersonCreateView, PersonListView

from . import views

# ######:8000/people/
urlpatterns = [
#    path('', views.simple_view),
    path('', PersonHomeView.as_view(), name='home'),
    path('person_create/', PersonCreateView.as_view(), name='create_person'),
    path('person_list/', PersonListView.as_view(), name='list_person'),
    path('person_list_battle/', NewPersonBattleListView.as_view(), name='battle_list_person'),

]
