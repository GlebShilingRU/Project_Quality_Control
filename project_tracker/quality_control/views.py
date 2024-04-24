from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render


def index(request):
    return render(request, 'quality_control/index.html')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


def bug_list(request):
    bug_list = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bug_list})


class BugListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'


def feature_list(request):
    feature_list = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': feature_list})


class FeatureListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
