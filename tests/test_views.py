import datetime
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from expense_manager_app.models import Expense
from django.contrib.auth import get_user_model
from expense_manager_app.forms import RegisterForm


@pytest.fixture
def test_user(db):
    return User.objects.create_user(
        username="testuser",
        password="12345"
    )


@pytest.fixture
def test_expense(db, test_user):
    return Expense.objects.create(
        user=test_user,
        card="Visa",
        category="Grocery",
        expense_date="2023-12-01",
        amount=100.00,
        notes="Test notes"
    )


@pytest.mark.django_db
def test_register_view(client):
    url = reverse("register")
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context["form"], RegisterForm)

    user_data = {
        "username": "newuser",
        "first_name": "John",
        "last_name": "Doe",
        "email": "example@gmail.com",
        "password1": "complex_password",
        "password2": "complex_password"
    }
    response = client.post(url, data=user_data)
    assert response.status_code == 302
    assert response.url == reverse("login")

    user_model = get_user_model()
    assert user_model.objects.filter(username="newuser").exists()


@pytest.mark.django_db
def test_expense_list_view(client, test_user, test_expense):
    url = reverse("expense-list")
    response = client.get(url)

    # Test if it redirects to login page
    assert response.status_code == 302
    assert response["Location"] == "/login/?next=/"

    client.force_login(test_user)
    response = client.get(url)
    assert response.status_code == 200
    assert test_expense in response.context["expenses"]


@pytest.mark.django_db
def test_expense_search_view(client, test_user, test_expense):
    url = reverse("expense-search") + "?search-card=Visa"
    response = client.get(url)
    # Redirect to login page
    assert response.status_code == 302
    assert response["Location"] == f"/login/?next=/search/%3Fsearch-card%3DVisa"

    # Login as test user
    client.force_login(user=test_user)
    response = client.get(url)
    assert response.status_code == 200
    assert test_expense in response.context["expenses"]


@pytest.mark.django_db
def test_expense_detail_view(client, test_user, test_expense):
    url = reverse("expense-detail", kwargs={'pk': test_expense.pk})
    response = client.get(url)

    # Redirect user to login page
    assert response.status_code == 302
    assert response["Location"] == f"/login/?next={url}"

    # Login as test user
    client.force_login(user=test_user)
    response = client.get(url)
    assert response.status_code == 200
    assert "expense" in response.context


@pytest.mark.django_db
def test_expense_create_view(client, test_user, test_expense):
    url = reverse("expense-add")
    response = client.get(url)

    # Redirect user to login page
    assert response.status_code == 302
    assert response["Location"] == f"/login/?next={url}"

    # Login as test user
    client.force_login(user=test_user)
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "expense_manager_app/expense_form.html")

    # Set up new expense data
    new_expense_data = {
        "card": "Mastercard",
        "category": "Utilities",
        "expense_date": datetime.date(2023, 12, 4),
        "amount": 200.00,
        "notes": "Test add"
    }
    response = client.post(url, new_expense_data)
    # Redirect to expense list page
    assert response.status_code == 302

    # Verify a new Expense object has been created
    new_expense = Expense.objects.last()
    assert new_expense is not None
    assert new_expense.user == test_user
    assert new_expense.card == "Mastercard"
    assert new_expense.category == "Utilities"
    assert str(new_expense.expense_date) == "2023-12-04"
    assert new_expense.amount == 200.00
    assert new_expense.notes == "Test add"


@pytest.mark.django_db
def test_expense_update_view(client, test_user, test_expense):
    url = reverse("expense-update", kwargs={"pk": test_expense.pk})
    response = client.get(url)

    # Redirect to login page
    assert response.status_code == 302
    assert response["Location"] == f"/login/?next={url}"

    # Login as test user
    client.force_login(test_user)

    # Verify initial form values (GET request)
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "expense_manager_app/expense_update_form.html")
    form = response.context.get("form")
    assert form.initial["card"] == test_expense.card

    # Perform update action
    updated_data = {
        "card": "Debit Card",
        "category": "Food",
        "expense_date": "2023-12-03",
        "amount": 50.00,
        "notes": "Test updating"
    }
    response = client.post(url, data=updated_data)

    # Redirect to expense list page
    assert response.status_code == 302
    assert response.url == reverse("expense-list")

    # Verify the update in the database
    test_expense.refresh_from_db()
    assert test_expense.card == "Debit Card"
    assert test_expense.category == "Food"
    assert test_expense.expense_date == datetime.date(2023, 12, 3)
    assert test_expense.amount == 50.00
    assert test_expense.notes == "Test updating"
    assert Expense.objects.filter(card="Debit Card").exists()


@pytest.mark.django_db
def test_expense_delete_view(client, test_user, test_expense):
    url = reverse("expense-delete", kwargs={"pk": test_expense.pk})
    response = client.get(url)

    # Redirect to login page
    assert response.status_code == 302
    assert response["Location"] == f"/login/?next={url}"

    # Login as test user
    client.force_login(user=test_user)

    # Verify the delete confirmation page
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "expense_manager_app/expense_confirm_delete.html")

    # Perform delete action
    response = client.post(url)

    # Redirect to expense list page after deleting expense
    assert response.status_code == 302
    assert response.url == reverse("expense-list")
    assert not Expense.objects.filter(pk=test_expense.pk).exists()
