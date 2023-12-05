from django.urls import reverse, resolve
from expense_manager_app import views
from django.contrib.auth import views as auth_views


def test_register_url():
    url = reverse("register")
    assert resolve(url).func.view_class == views.UserRegisterView


def test_login_url():
    url = reverse("login")
    assert resolve(url).func.view_class == auth_views.LoginView


def test_logout_url():
    url = reverse("logout")
    assert resolve(url).func.view_class == auth_views.LogoutView


def test_expense_list_url():
    url = reverse("expense-list")
    assert resolve(url).func.view_class == views.ExpenseListView


def test_expense_search_url():
    url = reverse("expense-search")
    assert resolve(url).func.view_class == views.ExpenseSearchView


def test_expense_detail_url():
    url = reverse("expense-detail", args=[1])
    assert resolve(url).func.view_class == views.ExpenseDetailView


def test_expense_add_url():
    url = reverse("expense-add")
    assert resolve(url).func.view_class == views.ExpenseCreateView


def test_expense_update_url():
    url = reverse("expense-update", args=[1])
    assert resolve(url).func.view_class == views.ExpenseUpdateView


def test_expense_delete_url():
    url = reverse("expense-delete", args=[1])
    assert resolve(url).func.view_class == views.ExpenseDeleteView
