# Generated by Django 2.2.17 on 2020-12-31 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("location", "0001_initial"),
        ("booking", "0005_bookingtransaction_dropoff4"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookingtransaction",
            name="dropoff5",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="bookingtransaction_dropoff5",
                to="location.MapLocation",
            ),
        ),
    ]
