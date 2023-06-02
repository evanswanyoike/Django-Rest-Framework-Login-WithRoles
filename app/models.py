from django.db import models
from django.contrib.auth.models import AbstractUser


class AdminProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    cookie = models.CharField(max_length=100, null=True, blank=True)
    repo = models.CharField(max_length=100, null=True, blank=True)
    frame = models.CharField(max_length=100, null=True, blank=True)
    additional = models.CharField(max_length=100, null=True, blank=True)
    # Add additional fields for admin profile


class TeacherProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    # Add additional fields for teacher profile


class StudentProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    # Add additional fields for student profile


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    # Add fields common to all user types
