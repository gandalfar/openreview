# Generated by Django 3.2.4 on 2021-06-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0002_entry"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="data",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
