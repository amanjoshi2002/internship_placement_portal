from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import InternshipListView, PlacementListView

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('internships/', InternshipListView.as_view(), name='internship_list'),
    path('placements/', PlacementListView.as_view(), name='placement_list'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Add this line
]
