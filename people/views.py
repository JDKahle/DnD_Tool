from django.shortcuts import render
from django.http import HttpResponse


from urllib import request
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Person
from django.shortcuts import get_object_or_404

from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

from . import models

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def simple_view(request):
    return HttpResponse('Hello!')

# Create your views here.
class PersonHomeView(TemplateView):
    template_name = 'people/home.html'


class PersonCreateView(CreateView):
    model = Person
    # model_form.html --> teacher_form.html
    fields = '__all__'
    success_url = reverse_lazy('people:list_person')

    def form_valid(self, form):     # Alles hier drin ist dafür verantwortlich, 
        obj = form.save(commit=False)   # dass ein sklave automatisch einen owner bekommt.
        obj.owner = self.request.user
        obj.save
        return super().form_valid(form)
