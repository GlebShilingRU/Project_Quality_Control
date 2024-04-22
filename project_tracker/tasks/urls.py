from django.urls import path
from tasks import views as tasks_views
from quality_control import views as quality_control_views

app_name = 'tasks'

urlpatterns = [
    path('', tasks_views.index),
    path('another/', tasks_views.another_page, name='another_page'),
    path('quality_control/', quality_control_views.index, name='quality_control'),
]