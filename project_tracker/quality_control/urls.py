from django.urls import path
from quality_control import views


app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/', views.feature_list, name='feature_list'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    path('bugs/new/', views.bug_report_form, name='bug_report_form'),
    path('features/new/', views.feature_request_form, name='feature_request_form'),
]
