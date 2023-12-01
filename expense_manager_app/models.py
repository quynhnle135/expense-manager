from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    expense_date = models.DateField(default=now())
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.card} -  {self.expense_date} - {self.amount}"