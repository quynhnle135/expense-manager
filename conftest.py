import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_manager.settings')
django.setup()