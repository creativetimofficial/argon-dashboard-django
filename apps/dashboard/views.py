from django.shortcuts import render
from .models import Dashboard, Widget


def dashboard_view(request, company_id=None):
    # If no company_id is provided, default to the first company or show an empty page
    dashboard = None
    widgets = None

    if company_id:
        dashboard = Dashboard.objects.filter(company_id=company_id).first()
        widgets = Widget.objects.filter(dashboard=dashboard).order_by('position')

    return render(request, 'dashboard.html', {'dashboard': dashboard, 'widgets': widgets})
