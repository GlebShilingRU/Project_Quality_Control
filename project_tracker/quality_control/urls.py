from django.urls import path
from quality_control import views as quality_control_views
from tasks import views as tasks_views


app_name = 'quality_control'

urlpatterns = [
    path('', quality_control_views.index, name='index'),
    path('bugs/', quality_control_views.bug_list, name='bug_list'),
    path('bugs/<int:bug_id>/', quality_control_views.bug_detail, name='bug_detail'),
    path('features/', quality_control_views.feature_list, name='feature_list'),
    path('features/<int:feature_id>/', quality_control_views.feature_detail, name='feature_detail'),
    path('tasks/', tasks_views.index, name='tasks')
]
