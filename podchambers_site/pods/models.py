from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
# Create your models here.


class Forum(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "A", "Active"
        INACTIVE = "I", "Inactive"
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    owner = models.ForeignKey(
        User,
        related_name='forums_managed',
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    main_color_integer = models.BigIntegerField(default=16777215)
    accent_color_integer = models.BigIntegerField(default=1769472)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['status', 'public']),
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return self.name

    def color_hex(self, color_int):
        return str(hex(color_int)).replace('0x', '#')


class ForumUser(models.Model):
    handle = models.CharField()
