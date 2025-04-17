from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, DeleteView, UpdateView

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
    _customer = None

    def get_queryset(self):
        qs = super().get_queryset()
        customer_pk = self.request.GET.get('customer', None)
        if customer_pk:
            self._customer = Customer.objects.get(pk=customer_pk)
            qs = qs.filter(customer=self._customer)
        return qs

    # display as list of items if ?list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = self._customer
        return context


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/create_update.html'
    context_object_name = 'project'
    fields = ['title', 'description', 'customer']

    def get_success_url(self):
        return reverse_lazy('project-list', kwargs={'customer': self.object.customer.pk})


class HttpResponseSeeOther(HttpResponseRedirect):
    status_code = 303


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/create_update.html'
    context_object_name = 'project'
    fields = ['title', 'description', 'customer']

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseSeeOther(success_url)

    def get_success_url(self):
        return reverse_lazy('project-list', kwargs={'customer': self.object.customer.pk})

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/detail.html'
    context_object_name = 'project'

    def get_success_url(self):
        return reverse_lazy('project-list', kwargs={'customer': self.object.customer.pk})


class CustomerDashboardView(TemplateView):
    """
    This should be a dashboard.
    Latest project detail, Customer stats, all the user's projects.
    """
    template_name = 'customer/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_id = self.kwargs.get('pk')
        context['latest_project_pk'] = Project.objects.filter(customer__pk=customer_id).latest().pk
        return context

class CustomerStatsView(DetailView):
    model = Customer
    template_name = 'customer/stats.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects_created_by_month"] = self.object.projects.values('created_on__month').annotate(
            count=Count('id')
        ).order_by('created_on__month')
        return context
