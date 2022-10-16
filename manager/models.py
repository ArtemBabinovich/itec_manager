from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    SEX_CHOICES = [
        ("Муж.", "Мужчина"),
        ("Жен.", "Женщина")
    ]

    sex = models.CharField(verbose_name="Пол", max_length=4, choices=SEX_CHOICES)
    phone = models.CharField(verbose_name="Номер телефона", unique=True, blank=True, null=True, max_length=13)
    birthday = models.DateField(verbose_name="День рождения", blank=True, null=True)
    interests = models.TextField(verbose_name="Интересы", blank=True, null=True, max_length=500)
    is_teacher = models.BooleanField(verbose_name="Преподаватель", default=False)
    is_student = models.BooleanField(verbose_name="Студент", default=False)


class Course(models.Model):
    name = models.CharField(verbose_name='Название курса', max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    start_date = models.DateField(verbose_name="День начала")
    finish_date = models.DateField(verbose_name="День окончания")
    teacher = models.ForeignKey('CustomUser',
                                on_delete=models.CASCADE,
                                limit_choices_to={'is_teacher': True},
                                related_name='teachers')
    group_size = models.PositiveIntegerField(verbose_name='Состав группы')
    group_members = models.ManyToManyField('CustomUser',
                                           related_name='group_members')
