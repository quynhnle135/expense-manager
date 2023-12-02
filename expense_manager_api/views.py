from rest_framework import generics
from .serializers import ExpenseSerializer
from expense_manager_app.models import Expense
from rest_framework import permissions
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter


class ExpenseFilter(filters.FilterSet):
    class Meta:
        model = Expense
        fields = {
            "card": ["icontains"],
            "category": ["icontains"],
            "notes": ["icontains"],
            "expense_date": ["icontains"],
            "amount": ["iexact"]
        }


class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = ExpenseFilter
    search_fields = ["card", "category", "notes", "expense_date", "amount"]

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)


class ExpenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permissions_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)
