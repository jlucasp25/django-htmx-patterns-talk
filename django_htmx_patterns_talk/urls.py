"""
URL configuration for django_htmx_patterns_talk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from core.views import CustomerListView, HomeDashboardView, ProjectListView, ProjectCreateView, ProjectUpdateView, \
    ProjectDetailView, CustomerDashboardView, CustomerStatsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeDashboardView.as_view(), name="home"),
    path("customers/", CustomerListView.as_view(), name="customer-list"),
    path("customer/<int:pk>/", CustomerDashboardView.as_view(), name="customer-dashboard"),
    path("customer/stats/<int:pk>/", CustomerStatsView.as_view(), name="customer-stats"),
    path("project/", ProjectCreateView.as_view(), name="project-create"),
    path("project/<int:pk>/", ProjectUpdateView.as_view(), name="project-update"),
    path("project/detail/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
]
