# Generated by Django 3.2.9 on 2021-11-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hours", "0015_change_some_model_options_and_verbose_names"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalresource",
            name="date_periods_hash",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="resource",
            name="date_periods_hash",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
