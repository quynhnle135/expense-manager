from django.urls import path
from . import views

urlpatterns = [
    path("expenses/", views.ExpenseListCreateView.as_view()),
    path("expenses/<int:pk>/", views.ExpenseRetrieveUpdateDestroyAPIView.as_view())
]