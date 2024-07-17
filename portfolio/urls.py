from django.urls import path
from . import views
from .views import SkillListView, SkillCreateView, SkillUpdateView, SkillDeleteView,ProjectListView,resume_view,delete_document,contact_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', SkillListView.as_view(), name='skills-list'),
    path('skills/add/', SkillCreateView.as_view(), name='skill-add'),
    path('skills/<int:pk>/update/', SkillUpdateView.as_view(), name='skill-update'),
    path('skills/<int:pk>/delete/', SkillDeleteView.as_view(), name='skill-delete'),
    path('projects/', views.ProjectListView.as_view(), name='projects-list'),
    path('projects/add/', views.ProjectCreateView.as_view(), name='project-add'),
    path('projects/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
    path('resume/', resume_view, name='resume'),
    path('delete_document/<int:document_id>/', delete_document, name='delete_document'),
    path('contact/', contact_view, name='contact'),
]
