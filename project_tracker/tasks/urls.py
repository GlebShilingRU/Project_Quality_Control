from django.urls import path
from tasks import views as tasks_views
from quality_control import views as quality_control_views

app_name = 'tasks'

urlpatterns = [
    path('', quality_control_views.IndexView.as_view(), name='index'),
    path('quality_control/', quality_control_views.index, name='quality_control'),
    path('projects/', tasks_views.ProjectListView.as_view(), name='projects_list'),
    path('projects/<int:project_id>/', tasks_views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', tasks_views.TaskDetailView.as_view(), name='task_detail'),
]