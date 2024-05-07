from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Internship, Placed, Placement



class InternshipListView(LoginRequiredMixin, ListView):
    model = Internship
    template_name = 'internship.html'
    context_object_name = 'internships'

    def get_success_url(self):
        return reverse_lazy('internship_list')

class PlacementListView(LoginRequiredMixin, ListView):
    model = Placement
    template_name = 'placement.html'
    context_object_name = 'placements'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['placed_students'] = Placed.objects.all()  # Retrieve all placed students
        return context
