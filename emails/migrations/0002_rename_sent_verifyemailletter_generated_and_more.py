# Generated by Django 4.2.7 on 2024-01-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="verifyemailletter",
            old_name="sent",
            new_name="generated",
        ),
        migrations.AlterField(
            model_name="verifyemailletter",
            name="code",
            field=models.IntegerField(editable=False),
        ),
    ]