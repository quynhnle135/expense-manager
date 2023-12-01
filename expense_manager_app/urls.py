from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="expense_manager_app/login.html", next_page="expense-list"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register, name="register"),
    path("expenses/", views.ExpenseListView.as_view(), name="expense-list"),
    path("expenses/<int:pk>/", views.ExpenseDetailView.as_view(), name="expense-detail"),
    path("expenses/new/", views.ExpenseCreateView.as_view(), name="expense-add"),
    path("expenses/update/<int:pk>/", views.ExpenseUpdateView.as_view(), name="expense-update"),
    path("expenses/delete/<int:pk>/", views.ExpenseDeleteView.as_view(), name="expense-delete")
]