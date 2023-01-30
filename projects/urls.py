from django.urls import path

from . import views
app_name = 'projects'
urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>/',
         views.updateProject, name="update-project"),
    path('project-delete/<str:pk>/',
         views.deleteProject, name="project-delete"),
    path('project-delete-confirm/<str:pk>/',
         views.deleteProjectConfirm, name="project-delete-confirm"),
]
