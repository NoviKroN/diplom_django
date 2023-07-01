# Generated by Django 4.2.2 on 2023-07-01 05:30

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
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(default='app_users/avatars/default.png', upload_to='app_users/avatars/user_avatars/', verbose_name='Ссылка')),
                ('alt', models.CharField(max_length=128, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Аватар',
                'verbose_name_plural': 'Аватары',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=128, verbose_name='Полное имя')),
                ('phone', models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='Номер телефона')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Баланс')),
                ('avatar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='custom_auth.avatar', verbose_name='Аватар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
