from django.urls import path

from . import views_projects
app_name = 'projects'
urlpatterns = [
    path('', views_projects.projects, name="projects"),
    path('project/<str:pk>/', views_projects.project, name="project"),
    path('create-project/', views_projects.createProject, name="create-project"),
    path('update-project/<str:pk>/',
         views_projects.updateProject, name="update-project"),
    path('project-delete/<str:pk>/',
         views_projects.deleteProject, name="project-delete"),
    path('project-delete-confirm/<str:pk>/',
         views_projects.deleteProjectConfirm, name="project-delete-confirm"),
]
