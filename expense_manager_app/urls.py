from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # User login/logout/register functions
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="expense_manager_app/login.html", next_page="expense-list"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    # Expense CRUD functions
    path("", views.ExpenseListView.as_view(), name="expense-list"),
    path("search/", views.ExpenseSearchView.as_view(), name="expense-search"),
    path("<int:pk>/", views.ExpenseDetailView.as_view(), name="expense-detail"),
    path("add/", views.ExpenseCreateView.as_view(), name="expense-add"),
    path("update/<int:pk>/", views.ExpenseUpdateView.as_view(), name="expense-update"),
    path("delete/<int:pk>/", views.ExpenseDeleteView.as_view(), name="expense-delete")
]