# manage.py
#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

# core/settings.py
SECRET_KEY = 'your-secret-key'
INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'accounts',
    'bookings'
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chibelle',
        'USER': 'chibelleuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# core/urls.py
from django.urls import path, include
urlpatterns = [
    path('', include('accounts.urls')),
    path('bookings/', include('bookings.urls')),
]

# accounts/models.py
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass

# accounts/urls.py
from django.urls import path
from django.http import JsonResponse

def healthcheck(request):
    return JsonResponse({"message": "Accounts app working."})

urlpatterns = [
    path('', healthcheck)
]

# bookings/models.py
from django.db import models
class Booking(models.Model):
    service = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
    user_id = models.IntegerField()

# bookings/urls.py
from django.urls import path
from django.http import JsonResponse

def test_booking(request):
    return JsonResponse({"message": "Booking API working."})

urlpatterns = [
    path('', test_booking)
]

# requirements.txt
Django>=4.2
djangorestframework
psycopg2-binary

# .env.example
SECRET_KEY=your-django-secret-key
DB_NAME=chibelle
DB_USER=chibelleuser
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

# fixtures/test_users.json
[
  {
    "model": "accounts.user",
    "pk": 1,
    "fields": {
      "username": "admin",
      "email": "admin@chibelle.com",
      "is_superuser": true,
      "is_staff": true,
      "is_active": true,
      "password": "pbkdf2_sha256$260000$demo$9aV2FvM0uOzFUZK9NRhRujq0cz5K9guEFzWz5V5EzKs="
    }
  }
]
