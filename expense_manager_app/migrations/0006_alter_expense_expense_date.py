# Generated by Django 4.2.7 on 2023-12-01 17:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager_app', '0005_alter_expense_expense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]