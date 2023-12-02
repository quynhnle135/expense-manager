from expense_manager_app.models import Expense
from rest_framework import serializers


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "card", "amount", "expense_date", "category", "notes"]