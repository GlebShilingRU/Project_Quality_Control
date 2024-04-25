from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import BugReportForm, FeatureRequestForm


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

def bug_report_form(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bug_list')


def feature_request_form(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:feature_list')


def update_bug_report(request, bug_report_id):
    bug_report = get_object_or_404(BugReport, pk=bug_report_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug_report)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm(instance=bug_report)
    return render(request, 'quality_control/bug_report_update.html', {'form': form, 'bug_report': bug_report})


class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_update.html'
    pk_url_kwarg = 'bug_report_id'
    success_url = reverse_lazy('quality_control:bug_list')


def update_feature_request(request, feature_request_id):
    feature_request = get_object_or_404(FeatureRequest, pk=feature_request_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature_request)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail')
    else:
        form = FeatureRequestForm(instance=feature_request)
    return render(request, 'quality_control/feature_request_update.html', {'form': form, 'feature_request': feature_request})


class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_update.html'
    pk_url_kwarg = 'feature_request_id'
    success_url = reverse_lazy('quality_control:feature_list')


def delete_bug_report(request, bug_report_id):
    bug_report = get_object_or_404(BugReport, pk=bug_report_id)
    bug_report.delete()
    return redirect('quality_control:bug_list')


class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_report_id'
    success_url = reverse_lazy('quality_control:bug_list')
    template_name = 'quality_control:bug_confirm_delete'


def delete_feature_request(request, feature_request_id):
    feature_request = get_object_or_404(BugReport, pk=feature_request_id)
    feature_request.delete()
    return redirect('quality_control:feature_list')


class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_request_id'
    success_url = reverse_lazy('quality_control:feature_list')
    template_name = 'quality_control:feature_confirm_delete'
