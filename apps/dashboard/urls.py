from django.urls import path
from apps.dashboard import views

urlpatterns = [
    path('dashboard/<int:company_id>/', views.dashboard_view, name='dashboard'),
]
