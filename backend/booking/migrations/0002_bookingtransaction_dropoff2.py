# Generated by Django 2.2.17 on 2020-12-31 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff2',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]