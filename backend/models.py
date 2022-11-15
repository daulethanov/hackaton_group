from django.contrib.auth.models import User, AbstractUser
from django.db import models


STREET = (
    ('SARAN', 'Сарань'),
    ('KAZ_BY', 'Казыбек Би'),
    ('MAIKEN', 'Майкудук'),
    ('JBI', 'ЖБИ'),
    ('SHAHTINSK', 'Шахтинск'),
    ('ABAY', 'Абай'),
    ('TEMIRTAU', 'Темиртау'),
)


class FullUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField('Город', choices=STREET, default='KAZ_BY', max_length=100)
    job_title = models.CharField('Должность', max_length=120)
    date_birth = models.DateField('Дата рождения')
    last_name = models.CharField('Фамилия', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)


class Team(models.Model):
    name = models.CharField(max_length=30)
    users_group = models.ManyToManyField(User, blank=True, null=True)
