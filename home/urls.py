from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('candidate/<int:id>', views.Candidate, name='candidate'),
]
