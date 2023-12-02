from rest_framework import generics
from .serializers import ExpenseSerializer
from expense_manager_app.models import Expense
from rest_framework import permissions


# Create your views here.
class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExpenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permissions_class = [permissions.IsAuthenticated]
