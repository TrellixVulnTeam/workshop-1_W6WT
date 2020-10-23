from django.urls import path

from  .  import views 

urlpatterns = [
  path('', views.index, name="index"),
  path('projects/', views.projects_list, name="Project List"),
  path('<int:project.id>/', views.current_project, name="current_projects"),
  path('user/', views.user_account, name="User"),
  path('teams/', views.teams, name="teams"),
]