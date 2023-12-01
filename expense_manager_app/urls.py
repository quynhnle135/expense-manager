from django.urls import path
from . import views

urlpatterns = [
    path("expenses/", views.ExpenseListView.as_view(), name="expense-list"),
    path("expenses/<int:pk>/", views.ExpenseDetailView.as_view(), name="expense-detail"),
    path("expenses/new/", views.ExpenseCreateView.as_view(), name="expense-add"),
    path("expenses/update/<int:pk>/", views.ExpenseUpdateView.as_view(), name="expense-update"),
    path("expenses/delete/<int:pk>/", views.ExpenseDeleteView.as_view(), name="expense-delete")
]