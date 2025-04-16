from django.views.generic import ListView, TemplateView, DetailView

from core.models import Customer, Project


class HomeDashboardView(TemplateView):
    template_name = 'home.html'
    entry_template_name = 'entry.html'

    def get_template_names(self):
        if self.request.htmx:
            return self.template_name
        return self.entry_template_name


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/list.html'
    context_object_name = 'customers'


class ProjectListView(ListView):
    model = Project
    template_name = 'project/list.html'
    context_object_name = 'projects'


class CustomerDashboardView(TemplateView):
    """
    This should be a dashboard.
    Latest project detail, Customer stats, all the user's projects.
    """
    pass
