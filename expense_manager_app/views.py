from django.views import generic
from .models import Expense
from django.urls import reverse_lazy


# Create your views here.
class ExpenseListView(generic.ListView):
    model = Expense
    context_object_name = "expenses"
    template_name = "expense_manager_app/expense_list.html"


class ExpenseDetailView(generic.DetailView):
    model = Expense
    context_object_name = "expense"
    template_name = "expense_manager_app/expense_detail.html"


class ExpenseCreateView(generic.CreateView):
    model = Expense
    fields = "__all__"
    template_name = "expense_manager_app/expense_form.html"
    success_url = reverse_lazy("expense-list")


class ExpenseUpdateView(generic.UpdateView):
    model = Expense
    fields = "__all__"
    template = "expense_manager_app/expense_update_form.html"
    success_url = reverse_lazy("expense-list")


class ExpenseDeleteView(generic.DeleteView):
    model = Expense
    template = ""
    success_url = reverse_lazy("expense-list")
    template_name = "expense_manager_app/expense_confirm_delete.html"
