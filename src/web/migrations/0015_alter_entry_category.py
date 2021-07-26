# Generated by Django 3.2.5 on 2021-07-26 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0014_entry_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="web.category",
            ),
        ),
    ]
