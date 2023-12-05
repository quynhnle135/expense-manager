import pytest
from django.contrib.auth.models import User
from expense_manager_app.models import Expense
from datetime import date


@pytest.fixture
def test_user(db):
    return User.objects.create_user(username="testuser", password="12345")


@pytest.mark.django_db
def test_expense_creation(test_user):
    expense = Expense.objects.create(
        user=test_user,
        card="Visa",
        category="Grocery",
        expense_date=date(2023, 12, 1),
        amount=100.00,
        notes="Thanksgiving party"
    )

    assert expense.user.username == "testuser"
    assert expense.card == "Visa"
    assert expense.category == "Grocery"
    assert expense.expense_date == date(2023, 12, 1)
    assert expense.amount == 100.00
    assert expense.notes == "Thanksgiving party"


@pytest.mark.django_db
def test_expense_str(test_user):
    expense = Expense.objects.create(
        user=test_user,
        card="Visa",
        category="Grocery",
        expense_date=date(2023, 12, 1),
        amount=100.00,
        notes="Thanksgiving party"
    )
    expense_str = str(expense)
    assert expense_str == "Visa - 2023-12-01 - 100.0"