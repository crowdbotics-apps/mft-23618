# Generated by Django 2.2.17 on 2020-12-31 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('booking', '0009_auto_20201231_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff41',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff41', to='location.MapLocation'),
        ),
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff42',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff42', to='location.MapLocation'),
        ),
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff43',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff43', to='location.MapLocation'),
        ),
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff44',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff44', to='location.MapLocation'),
        ),
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff45',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff45', to='location.MapLocation'),
        ),
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff46',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff46', to='location.MapLocation'),
        ),
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff47',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff47', to='location.MapLocation'),
        ),
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff48',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff48', to='location.MapLocation'),
        ),
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff49',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff49', to='location.MapLocation'),
        ),
        migrations.AddField(
            model_name='bookingtransaction',
            name='dropoff50',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookingtransaction_dropoff50', to='location.MapLocation'),
        ),
    ]
