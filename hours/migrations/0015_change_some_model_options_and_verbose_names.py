# Generated by Django 3.2.9 on 2021-11-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hours", "0014_add_created_modified_indexes"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dateperiod",
            options={
                "ordering": ["start_date"],
                "verbose_name": "Period",
                "verbose_name_plural": "Periods",
            },
        ),
        migrations.AlterModelOptions(
            name="timespan",
            options={
                "ordering": [
                    "weekdays",
                    "start_time",
                    "end_time_on_next_day",
                    "end_time",
                    "resource_state",
                ],
                "verbose_name": "Time span",
                "verbose_name_plural": "Time spans",
            },
        ),
        migrations.AlterField(
            model_name="datasource",
            name="user_editable_organizations",
            field=models.BooleanField(
                default=False, verbose_name="Organizations may be edited by users"
            ),
        ),
        migrations.AlterField(
            model_name="historicaldatasource",
            name="user_editable_organizations",
            field=models.BooleanField(
                default=False, verbose_name="Organizations may be edited by users"
            ),
        ),
    ]