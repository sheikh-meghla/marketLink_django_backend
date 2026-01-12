
import os
import django
import sys

# Setup Django environment
sys.path.append('c:\\Users\\sheik\\meghla\\marketLink_django_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketLink_django_backend.settings')
django.setup()

try:
    from apps.user.serializers import SignUpSerializer
    print("SUCCESS: SignUpSerializer imported successfully.")
except Exception as e:
    print(f"FAILED: {e}")
