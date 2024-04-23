from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404


def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    tasks_url = reverse('quality_control:tasks')
    html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><p><a href='{feature_list_url}'>Список запросов на улучшение</a></p><p><a href='{tasks_url}'>Страница приложения tasks</a></p>"
    return HttpResponse(html)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        tasks_url = reverse('quality_control:tasks')
        html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br /><a href='{feature_list_url}'>Список запросов на улучшение</a><br /><a href='{tasks_url}'>Страница приложения tasks</a>"
        return HttpResponse(html)

def bug_list(request):
    bug_reports = BugReport.objects.all()
    bug_report_html = '<h1>Список отчётов об ошибках</h1><ul>'
    for bug_report in bug_reports:
        bug_report_html += f'<li><a href="{bug_report.id}/">{bug_report.title}</a> ({bug_report.status})</li>'
    bug_report_html += '</ul>'
    return HttpResponse(bug_report_html)

def feature_list(request):
    feature_requests = FeatureRequest.objects.all()
    feature_request_html = '<h1>Список фич</h1><ul>'
    for feature_request in feature_requests:
        feature_request_html += f'<li><a href="{feature_request.id}/">{feature_request.title}</a> ({feature_request.status})</li>'
    feature_request_html += '</ul>'
    return HttpResponse(feature_request_html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug_report = self.object
        project = bug_report.project
        task = bug_report.task
        response_html = f'<h1>{bug_report.title}</h1><p>Описание: {bug_report.description}</p><p>Статус: {bug_report.status}</p><p>Приоритет: {bug_report.priority}</p><p>Проект: {project}</p><p>Задача: {task}</p>'
        return HttpResponse(response_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature_request = self.object
        project = feature_request.project
        task = feature_request.task
        response_html = f'<h1>{feature_request.title}</h1><p>Описание: {feature_request.description}</p><p>Статус: {feature_request.status}</p><p>Приоритет: {feature_request.priority}</p><p>Проект: {project}</p><p>Задача: {task}</p>'
        return HttpResponse(response_html)
