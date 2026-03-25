from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student Intern'),
        ('workplace_supervisor', 'Workplace Supervisor'),
        ('academic_supervisor', 'Academic Supervisor'),
        ('internship_admin', 'Internship Administrator'),
        ('system_admin', 'System Administrator'),
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

# Create your models here.
