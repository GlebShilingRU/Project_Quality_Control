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
    #path('bugs/new/', views.BugReportCreateView.as_view(), name='bug_report_form'),
    #path('features/new/', views.FeatureRequestCreateView.as_view(), name='feature_request_form'),
    path('bugs/<int:bug_report_id>/update/', views.update_bug_report, name='update_bug_report'),
    path('features/<int:feature_request_id>/update/', views.update_feature_request, name='update_feature_request'),
    #path('bugs/<int:bug_report_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug_report'),
    #path('features/<int:feature_request_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature_request'),
    path('bugs/<int:bug_report_id>/delete/', views.delete_bug_report, name='delete_bug_report'),
    path('features/<int:feature_request_id>/delete/', views.delete_feature_request, name='delete_feature_request'),
    #path('bugs/<int:bug_report_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug_report'),
    #path('features/<int:feature_request_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature_request'),
]
