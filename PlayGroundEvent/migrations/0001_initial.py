# Generated by Django 4.1.1 on 2022-09-20 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Наименование организации')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('date', models.DateField(null=True, verbose_name='Дата проведения')),
                ('ticket_count', models.PositiveIntegerField(verbose_name='Количество билетов')),
                ('organizer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event', to='PlayGroundEvent.company', verbose_name='Организатор')),
                ('sponsors', models.ManyToManyField(related_name='+', to='PlayGroundEvent.company', verbose_name='Спонсоры')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('number', models.PositiveIntegerField(verbose_name='Номер билета')),
                ('vip', models.BooleanField(verbose_name='Статус билета "ВИП"')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayGroundEvent.event', verbose_name='Название мероприятия')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Посетитель')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
