from django.views.generic import ListView

from core.models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/list.html'
    context_object_name = 'customers'