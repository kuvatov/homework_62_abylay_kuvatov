# Generated by Django 4.1.7 on 2023-03-10 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0017_alter_issue_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="project",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="issues",
                to="webapp.project",
                verbose_name="Проект",
            ),
            preserve_default=False,
        ),
    ]