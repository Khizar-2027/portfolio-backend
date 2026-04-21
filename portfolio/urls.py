from django.urls import path
from .views import SkillListView, ProjectListView, ProjectDetailView, ContactView

urlpatterns = [
    path('skills/', SkillListView.as_view()),
    path('projects/', ProjectListView.as_view()),
    path('projects/<slug:slug>/', ProjectDetailView.as_view()),
    path('contact/', ContactView.as_view()),
]
