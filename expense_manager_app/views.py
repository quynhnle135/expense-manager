from django.contrib.auth import login
from django.views import generic
from .models import Expense
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import FormView
from . import forms
from django.db.models import Q
from datetime import datetime
from django.db.models import Sum


class UserRegisterView(FormView):
    form_class = forms.RegisterForm
    template_name = "expense_manager_app/register.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class ExpenseListView(LoginRequiredMixin, generic.ListView):
    login_url = "/login/"
    model = Expense
    context_object_name = "expenses"
    template_name = "expense_manager_app/expense_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["expenses"] = Expense.objects.filter(user=self.request.user)
        context["count"] = Expense.objects.filter(user=self.request.user).count()
        total_amount = Expense.objects.filter(user=self.request.user).aggregate(total=Sum('amount'))['total']
        context["total"] = round(total_amount, 2) if total_amount is not None else 0
        return context

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ExpenseSearchView(LoginRequiredMixin, generic.ListView):
    login_url = "/login/"
    model = Expense
    template_name = "expense_manager_app/expense_search_list.html"
    context_object_name = "expenses"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(user=self.request.user)
        queryset = self.get_queryset()
        context["count"] = queryset.count()
        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)

        search_card = self.request.GET.get("search-card") or ""
        search_category = self.request.GET.get("search-category") or ""
        search_date = self.request.GET.get("search-date") or ""
        search_amount = self.request.GET.get("search-amount") or ""
        search_notes = self.request.GET.get("search-notes") or ""

        query = Q()

        if search_card:
            query &= Q(card__icontains=search_card)
        if search_category:
            query &= Q(category__icontains=search_category)
        if search_date:
            try:
                date_obj = datetime.strptime(search_date, "%Y-%m-%d")
                query &= Q(date__date=date_obj)
            except ValueError:
                pass
        if search_amount:
            query &= Q(amount__exact=search_amount)
        if search_notes:
            query &= Q(notes__icontains=search_notes)

        return queryset.filter(query) if query else queryset


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

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class ExpenseUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = "/login/"
    model = Expense
    fields = ["card", "category", "expense_date", "amount", "notes"]
    template_name = "expense_manager_app/expense_update_form.html"
    success_url = reverse_lazy("expense-list")


class ExpenseDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = "/login/"
    model = Expense
    template_name = "expense_manager_app/expense_confirm_delete.html"
    success_url = reverse_lazy("expense-list")
