from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    SEX_CHOICES = [
        ("Муж.", "Мужчина"),
        ("Жен.", "Женщина")
    ]

    sex = models.CharField(verbose_name="Пол", max_length=4, choices=SEX_CHOICES)
    phone = models.CharField(verbose_name="Номер телефона", unique=True, blank=True, null=True, max_length=13)
    birthday = models.DateField(verbose_name="День рождения", blank=True, null=True,)
    interests = models.TextField(verbose_name="Интересы", blank=True, null=True, max_length=500)
    is_teacher = models.BooleanField(verbose_name="Преподаватель", default=False)
    is_student = models.BooleanField(verbose_name="Студент", default=False)
