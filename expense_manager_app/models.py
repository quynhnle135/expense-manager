from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    expense_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(null=True, blank=True)

