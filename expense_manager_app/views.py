from django.shortcuts import redirect, render
from django.views import generic
from .models import Expense
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "expense_manager_app/register.html", {"form": form})


class ExpenseListView(LoginRequiredMixin, generic.ListView):
    login_url = "/login/"
    model = Expense
    context_object_name = "expenses"
    template_name = "expense_manager_app/expense_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = Expense.objects.filter(user=self.request.user)
        context["count"] = Expense.objects.filter(user=self.request.user).count()
        return context

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ExpenseDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = "/login/"
    model = Expense
    context_object_name = "expense"
    template_name = "expense_manager_app/expense_detail.html"


class ExpenseCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = "/login/"
    model = Expense
    fields = ["card", "category", "expense_date", "amount", "notes"]
    template_name = "expense_manager_app/expense_form.html"
    success_url = reverse_lazy("expense-list")


class ExpenseUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = "/login/"
    model = Expense
    fields = ["card", "category", "expense_date", "amount", "notes"]
    template = "expense_manager_app/expense_update_form.html"
    success_url = reverse_lazy("expense-list")


class ExpenseDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = "/login/"
    model = Expense
    template_name = "expense_manager_app/expense_confirm_delete.html"
    success_url = reverse_lazy("expense-list")
