# Generated by Django 4.2.7 on 2023-12-01 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager_app', '0004_alter_expense_expense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 1, 17, 1, 20, 559914, tzinfo=datetime.timezone.utc)),
        ),
    ]
