# Generated by Django 4.1.7 on 2023-03-21 07:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("webapp", "0021_project_users"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="users",
            field=models.ManyToManyField(
                related_name="projects",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователи",
            ),
        ),
    ]
