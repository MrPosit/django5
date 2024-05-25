# Generated by Django 5.0.6 on 2024-05-25 15:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(4, 'Длина должна быть более 4 символов.')])),
                ('author', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(4, 'Длина должна быть более 4 символов.')])),
                ('producer', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(4, 'Длина должна быть более 4 символов.')])),
                ('genre', models.CharField(choices=[('rock', 'Рок'), ('rap', 'Рэп'), ('classical', 'Классика'), ('jazz', 'Джаз'), ('metal', 'Метал'), ('pop', 'Поп'), ('other', 'Другое')], max_length=10)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1890, 'Не раньше 1890 года.'), django.core.validators.MaxValueValidator(2025, 'Не позже 2025 года')])),
                ('rating', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0, 'Принимается только положительные числа и ноль')])),
            ],
        ),
    ]