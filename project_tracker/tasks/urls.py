from django.urls import path
from tasks import views as tasks_views
from quality_control import views as quality_control_views

app_name = 'tasks'

urlpatterns = [
    path('', tasks_views.index, name='index'),
    path('projects/', tasks_views.projects_list, name='projects_list'),
    path('projects/<int:project_id>/', tasks_views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', tasks_views.task_detail, name='task_detail'),
]